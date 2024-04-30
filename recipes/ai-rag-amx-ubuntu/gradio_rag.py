import os
import pandas as pd
from langchain_community.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.embeddings import HuggingFaceEmbeddings
from datasets import load_dataset

import gradio as gr

# Defining paths to the different models 
model_paths = {
    "Falcon" : "/data/models/ggml-model-gpt4all-falcon-q4_0.bin",
    "Mistral" : "/data/models/mistral_model"
}
n_threads=64
max_tokens=200
repeat_penalty=1.50
n_batch=64
top_k=2
temp=0.7
chunk_size=500
overlap=50
rag_off= False

data_path = ""
index = ""
prompt = ""


datasets = {"robot maintenance": "FunDialogues/customer-service-robot-support", 
                "basketball coach": "FunDialogues/sports-basketball-coach", 
                "physics professor": "FunDialogues/academia-physics-office-hours",
                "grocery cashier" : "FunDialogues/customer-service-grocery-cashier",
                "Doctor": "FunDialogues/healthcare-minor-consultation"}

def download_dataset(datasets, chosen_dataset):
    """
    Downloads the specified dataset and saves it to the data path.

    Parameters
    ----------
    dataset : str
        The name of the dataset to be downloaded.
    """
    data_path = chosen_dataset + '_dialogues.txt'

    if not os.path.isfile(data_path):
        datasets = datasets
        # Download the dialogue from hugging face
        dataset = load_dataset(f"{datasets[chosen_dataset]}")
        # Convert the dataset to a pandas dataframe
        dialogues = dataset['train']
        df = pd.DataFrame(dialogues, columns=['id', 'description', 'dialogue'])
        # Print the first 5 rows of the dataframe
        df.head()
        # only keep the dialogue column
        dialog_df = df['dialogue']
        
        # save the data to txt file
        dialog_df.to_csv(data_path, sep=' ', index=False)
    else:
        print('data already exists in path.')     


def build_vectordb(chunk_size, overlap):
    """
    Builds a vector database from the dataset for retrieval purposes.

    Parameters
    ----------
    chunk_size : int
        The size of text chunks for vectorization.
    overlap : int
        The overlap size between chunks.
    """
    loader = TextLoader(data_path)
    # Text Splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    # Embed the document and store into chroma DB
    index = VectorstoreIndexCreator(embedding= HuggingFaceEmbeddings(), text_splitter=text_splitter).from_loaders([loader])

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

    user_input = user_input
    context_verbosity = False
            
    # perform a similarity search and retrieve the context from our documents
    results = index.vectorstore.similarity_search(user_input, k=top_k)
    # join all context information into one string 
    context = "\n".join([document.page_content for document in results])
    if context_verbosity:
        print(f"Retrieving information related to your question...")
        print(f"\nFound this content which is most similar to your question: {context}")

    if rag_off:
        template = """Question: {question}
        Answer: This is the response: """
        prompt = PromptTemplate(template=template, input_variables=["question"])
    else:     
        template = """ Don't just repeat the following context, use it in combination with your knowledge to improve your answer to the question:{context}

        Question: {question}
        """
        prompt = PromptTemplate(template=template, input_variables=["context", "question"]).partial(context=context)


callbacks = [StreamingStdOutCallbackHandler()]

#Setting and loading the default model
selected_model_path = model_paths["Falcon"]
llm = GPT4All(model=selected_model_path, callbacks=callbacks, verbose=False,
                    n_threads=n_threads, n_predict=max_tokens, repeat_penalty=repeat_penalty, 
                    n_batch=n_batch, top_k=top_k, temp=temp)

template = """Question: {question}
            Answer: This is the response: """

prompt = PromptTemplate(template=template, input_variables=["question"])
#prompt = PromptTemplate(template=template, input_variables=["context", "question"]).partial(context=context)

llm_chain = LLMChain(prompt=prompt, llm=llm)

def predict(question, selected_model, selected_dataset):
    # Load the selected dataset and build vectors
    #download_dataset(datasets, selected_dataset)
    data_path = selected_dataset + '_dialogues.txt'

    if not os.path.isfile(data_path):
        datasets = {"robot maintenance": "FunDialogues/customer-service-robot-support", 
                "basketball coach": "FunDialogues/sports-basketball-coach", 
                "physics professor": "FunDialogues/academia-physics-office-hours",
                "grocery cashier" : "FunDialogues/customer-service-grocery-cashier",
                "Doctor": "FunDialogues/healthcare-minor-consultation"}
        # Download the dialogue from hugging face
        dataset = load_dataset(f"{datasets[selected_dataset]}")
        # Convert the dataset to a pandas dataframe
        dialogues = dataset['train']
        df = pd.DataFrame(dialogues, columns=['id', 'description', 'dialogue'])
        # Print the first 5 rows of the dataframe
        df.head()
        # only keep the dialogue column
        dialog_df = df['dialogue']
        print("\nHead of Dialog_DF = ", dialog_df.head())
        # save the data to txt file
        dialog_df.to_csv(data_path, sep=' ', index=False)
    else:
        print('data already exists in path.')     

    #build_vectordb(chunk_size, overlap)
    loader = TextLoader(data_path)
    # Text Splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    # Embed the document and store into chroma DB
    index = VectorstoreIndexCreator(embedding= HuggingFaceEmbeddings(), text_splitter=text_splitter).from_loaders([loader])

    #retrieval_mechanism(user_input = question, top_k=2, rag_off=False)
    user_input = question
    context_verbosity = False
            
    # perform a similarity search and retrieve the context from our documents
    results = index.vectorstore.similarity_search(user_input, k=top_k)
    # join all context information into one string 
    context = "\n".join([document.page_content for document in results])
    if context_verbosity:
        print(f"Retrieving information related to your question...")
        print(f"\nFound this content which is most similar to your question: {context}")

    if rag_off:
        template = """Question: {question}
        Answer: This is the response: """
        prompt = PromptTemplate(template=template, input_variables=["question"])
    else:
        '''     
        template = """ Don't just repeat the following context, use it in combination with your knowledge to improve your answer to the question:{context}
        Question: {question}
        """
        '''
       #template = "Answer the question in a short and direct manner without including any unecessary information. You can remove quotes and information like [Agent/Person/Contact]:"   
        template = "Using the context, develop an answer to the question in a short and direct manner without including any unecessary information. Only incude the answer in the response and nothing extraneous"  
        prompt = PromptTemplate(template=template, input_variables=["context", "question"]).partial(context=context)

    print("\nThis is the Type returned from PromptTemplate:", type(prompt))
    print("\nThis is the Prompt returned from PromptTemplate:", prompt)
    #selected_data_path = datasets[selected_dataset]
    # Load the selected model
    selected_model_path = model_paths[selected_model]


    llm = GPT4All(model=selected_model_path, callbacks=callbacks, verbose=False,
                   n_threads=n_threads, n_predict=max_tokens, repeat_penalty=repeat_penalty,
                   n_batch=n_batch, top_k=top_k, temp=temp)
    llm_chain.llm = llm  # Update the llm in the LLMChain

    # Get the answer using the updated model
    answer = llm_chain.run(prompt)
    print("\n This is the answer returned by the LLM: ", answer)
    return answer

# Create a list of models for the dropdown
model_choices = list(model_paths.keys())
dataset_choices = list(datasets.keys())
'''
#question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"
def predict(question):
    answer = llm_chain.run(question)
    return answer
'''
iface = gr.Interface(
    fn=predict,
    inputs=[gr.Text("text"), gr.Dropdown(choices=model_choices, label="Select Model"), gr.Dropdown(choices=dataset_choices, label="Select RAG Dataset")],
    outputs="text",
    title="RAG Demo",
    description="Enter your question below:",
)
iface.launch(share=True)