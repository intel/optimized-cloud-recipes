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
max_tokens=100
repeat_penalty=1.50
n_batch=64
top_k=2
temp=0.7


datasets = {"robot maintenance": "FunDialogues/customer-service-robot-support", 
                "basketball coach": "FunDialogues/sports-basketball-coach", 
                "physics professor": "FunDialogues/academia-physics-office-hours",
                "grocery cashier" : "FunDialogues/customer-service-grocery-cashier",
                "Doctor": "FunDialogues/healthcare-minor-consultation"}

#setting and loading the default dataset
selected_data_path = datasets["robot maintenance"]
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



callbacks = [StreamingStdOutCallbackHandler()]

#Setting and loading the default model
selected_model_path = model_paths["Model 1"]
llm = GPT4All(model=selected_model_path, callbacks=callbacks, verbose=False,
                    n_threads=n_threads, n_predict=max_tokens, repeat_penalty=repeat_penalty, 
                    n_batch=n_batch, top_k=top_k, temp=temp)

template = """Question: {question}
            Answer: This is the response: """

prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt, llm=llm)


def predict(question, selected_model, selected_dataset):
    # Load the selected model
    selected_data_path = datasets[selected_dataset]
    selected_model_path = model_paths[selected_model]
    llm = GPT4All(model=selected_model_path, callbacks=callbacks, verbose=False,
                   n_threads=n_threads, n_predict=max_tokens, repeat_penalty=repeat_penalty,
                   n_batch=n_batch, top_k=top_k, temp=temp)
    llm_chain.llm = llm  # Update the llm in the LLMChain

    # Get the answer using the updated model
    answer = llm_chain.run(question)
    return answer

# Create a list of models for the dropdown
model_choices = list(model_paths.keys())
'''
#question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"
def predict(question):
    answer = llm_chain.run(question)
    return answer
'''
iface = gr.Interface(
    fn=predict,
    inputs=[gr.Text("text"), gr.Dropdown(choices=model_choices, label="Select Model")],
    outputs="text",
    title="RAG Demo",
    description="Enter your question below:",
)
iface.launch(share=True)