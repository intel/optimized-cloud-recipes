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

model_path = "/data/models/ggml-model-gpt4all-falcon-q4_0.bin"
n_threads=64
max_tokens=100
repeat_penalty=1.50
n_batch=64
top_k=2
temp=0.7




callbacks = [StreamingStdOutCallbackHandler()]

llm = GPT4All(model=model_path, callbacks=callbacks, verbose=False,
                    n_threads=n_threads, n_predict=max_tokens, repeat_penalty=repeat_penalty, 
                    n_batch=n_batch, top_k=top_k, temp=temp)

template = """Question: {question}
            Answer: This is the response: """

prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt, llm=llm)


question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

llm_chain.run(question)