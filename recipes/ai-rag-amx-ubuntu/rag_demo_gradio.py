# Intel® Corporation Copyright
# Contributors: William Fowler, Chris Ah-Siong, Joshua Segovia

import os
import pandas as pd
import gradio as gr

#from tqdm import tqdm
from langchain_community.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.embeddings import HuggingFaceEmbeddings
from datasets import load_dataset

# Initialize previous value variables
previous_threads = None
previous_max_tokens = None
previous_top_k = None
previous_dataset = None
previous_chunk_size = None
previous_overlap = None
previous_temp = None


#Adding gradio global variables
# Initialize RAGBot and prepare the model, dataset, and vector database
 

class RAGBot:
    """
    A class to handle model downloading, dataset management, model loading, vector database
    creation, retrieval mechanisms, and inference for a response generation bot.

    Attributes
    ----------
    model_path : str
        The file path where the model is stored.
    data_path : str
        The file path where the dataset is stored.
    user_input : str
        The input provided by the user for generating a response.
    model : str
        The name of the model being used.
    """

    def __init__(self):
        """
        Initializes the RAGBot with default values for model path, data path,
        user input, and model.
        """
        self.model_path = ""
        self.data_path = ""
        self.user_input = ""
        self.model = ""

    def get_model(self, model, chunk_size: int = 10000):
        """
        Downloads the specified model to the model path. Supports downloading of large
        models in chunks.

        Additional download tooling is reserved for users to add their own models. Currently hardcoded to load Falcon from 

        Parameters
        ----------
        model : str
            The name of the model to be downloaded.
        chunk_size : int, optional
            The size of each chunk of data to download at a time, by default 10000.
        """

        #model_hf = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-Chat-3B-v1", torch_dtype=torch.bfloat16)
        #self.model = model

        if self.model == "Falcon":
            self.model_path = "/data/models/ggml-model-gpt4all-falcon-q4_0.bin"
            print("Model path found: ", self.model_path)
            print("FALCON MODEL SELECTED AND SET TO VARIABLE SELF.MODEL_PATH! SELF.MODEL_PATH = ", self.model_path)
            #self.model_path = model_hf
        elif self.model == "Mistral":
            self.model_path = "/data/models/mistral_model"
            print("Model path found: ", self.model_path)
            print("MISTRAL MODEL SELECTED AND SET TO VARIABLE SELF.MODEL_PATH! SELF.MODEL_PATH = ", self.model_path)
        else:
            print("More models coming soon, defaulting to Falcon for now!")
            self.model_path = "/data/models/ggml-model-gpt4all-falcon-q4_0.bin"
            print("FALCON DEFAULTED! MODEL SELECTED AND SET TO VARIABLE SELF.MODEL_PATH! SELF.MODEL_PATH = ", self.model_path )
            #self.model_path = model_hf

    def download_dataset(self, dataset):
        """
        Downloads the specified dataset and saves it to the data path.

        Parameters
        ----------
        dataset : str
            The name of the dataset to be downloaded.
        """
        self.data_path = dataset + '_dialogues.txt'

        if not os.path.isfile(self.data_path):

            datasets = {"robot maintenance": "FunDialogues/customer-service-robot-support", 
                        "basketball coach": "FunDialogues/sports-basketball-coach", 
                        "physics professor": "FunDialogues/academia-physics-office-hours",
                        "grocery cashier" : "FunDialogues/customer-service-grocery-cashier",
                        "Doctor": "FunDialogues/healthcare-minor-consultation"}
            print(dataset)
            print("DATASET SELECTED:" , dataset)
            # Download the dialogue from hugging face
            dataset = load_dataset(f"{datasets[dataset]}")
            print("DATASET AFTER LOAD_DATASET FUNCTION:" , dataset)
            # Convert the dataset to a pandas dataframe
            dialogues = dataset['train']
            df = pd.DataFrame(dialogues, columns=['id', 'description', 'dialogue'])
            # Print the first 5 rows of the dataframe
            df.head()
            # only keep the dialogue column
            dialog_df = df['dialogue']
            
            # save the data to txt file
            dialog_df.to_csv(self.data_path, sep=' ', index=False)
        else:
            print('data already exists in path.')        

    def load_model(self, n_threads, max_tokens, repeat_penalty, n_batch, top_k, temp):
        """
        Loads the model with specified parameters for parallel processing.

        Parameters
        ----------
        n_threads : int
            The number of threads for parallel processing.
        max_tokens : int
            The maximum number of tokens for model prediction.
        repeat_penalty : float
            The penalty for repeated tokens in generation.
        n_batch : int
            The number of batches for processing.
        top_k : int
            The number of top k tokens to be considered in sampling.
        """
        # Callbacks support token-wise streaming
        callbacks = [StreamingStdOutCallbackHandler()]
        # Verbose is required to pass to the callback manager

        print("")
        print("Model path selected for loading into GPT4ALL FUNCTION: ", self.model_path)
        self.llm = GPT4All(model=self.model_path, callbacks=callbacks, verbose=False,
                           n_threads=n_threads, n_predict=max_tokens, repeat_penalty=repeat_penalty, 
                           n_batch=n_batch, top_k=top_k, temp=temp)
        
        print("MODEL LOADED! MODEL TYPE: ", type(self.llm))
        print("MODEL PATH/TYPE:", self.model_path)

    def build_vectordb(self, chunk_size, overlap):
        """
        Builds a vector database from the dataset for retrieval purposes.

        Parameters
        ----------
        chunk_size : int
            The size of text chunks for vectorization.
        overlap : int
            The overlap size between chunks.
        """
        loader = TextLoader(self.data_path)
        # Text Splitter
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
        # Embed the document and store into chroma DB
        self.index = VectorstoreIndexCreator(embedding= HuggingFaceEmbeddings(), text_splitter=text_splitter).from_loaders([loader])

    def retrieval_mechanism(self, user_input, top_k=1, context_verbosity = False, rag_off= False):
        """
        Retrieves relevant document snippets based on the user's query.

        Parameters
        ----------
        user_input : str
            The user's input or query.
        top_k : int, optional
            The number of top results to return, by default 1.
        context_verbosity : bool, optional
            If True, additional context information is printed, by default False.
        rag_off : bool, optional
            If True, disables the retrieval-augmented generation, by default False.
        """

        self.user_input = user_input
        self.context_verbosity = context_verbosity
                
        # perform a similarity search and retrieve the context from our documents
        results = self.index.vectorstore.similarity_search(self.user_input, k=top_k)
        # join all context information into one string 
        context = "\n".join([document.page_content for document in results])
        if self.context_verbosity:
            print(f"Retrieving information related to your question...")
            print(f"Found this content which is most similar to your question: {context}")

        if rag_off:
            template = """Question: {question}
            Answer: This is the response: """
            self.prompt = PromptTemplate(template=template, input_variables=["question"])
        else:     
            template = """ Don't just repeat the following context, use it in combination with your knowledge to improve your answer to the question:{context}

            Question: {question}
            """
            self.prompt = PromptTemplate(template=template, input_variables=["context", "question"]).partial(context=context)


    def inference(self):
        """
        Performs inference to generate a response based on the user's query.

        Returns
        -------
        str
            The generated response.
        """

        if self.context_verbosity:
            print(f"Your Query: {self.prompt}")
            
        llm_chain = LLMChain(prompt=self.prompt, llm=self.llm)
        print("Processing the information with gpt4all...\n")
        response = llm_chain.run(self.user_input)

        return  response  

#Initialize RAGBot for gradio

bot = RAGBot()
#model_dropdown = gr.inputs.Dropdown(, label="Model")
#dataset_dropdown = gr.inputs.Dropdown(["robot maintenance", "basketball coach", "physics professor", "grocery cashier", "Doctor"], label="Dataset")

model_dropdown = ["Falcon", "Mistral"]
dataset_dropdown = ["robot maintenance", "basketball coach", "physics professor", "grocery cashier", "Doctor"]

#Attepting to check textboxes
with gr.Blocks() as demo:
    d1 = gr.Dropdown(choices = model_dropdown, label="Choose Model")
    d2 = gr.Dropdown(choices = dataset_dropdown, label = "Choose dataset")        

    outputs = gr.Textbox()

    def print_results(d1, d2):
        return f"You selected '{d1}' in the first dropdown and '{d2}' in the second dropdown."
        
    d2.input(print_results, [d1, d2], outputs)

demo.launch(share=True)

'''
def run_rag(question, bot):
    bot.retrieval_mechanism(user_input = question, top_k=2, rag_off=False)
    result = bot.inference()
    return result

def handle_query(model, dataset, question):
    """
    Handles a user query by running the RAG model and returning the response.
    """
    bot.get_model(model)
    bot.download_dataset(dataset)
    bot.load_model(n_threads=64, max_tokens=100, repeat_penalty=1.50, n_batch=64, top_k=2, temp=0.7)
    bot.build_vectordb(chunk_size=500, overlap=50)
    result = run_rag(question, bot)
    return result

iface = gr.Interface(fn=handle_query, inputs=[model_dropdown, dataset_dropdown, "text"], outputs="text", title="Question Answering System")
iface.launch()
'''