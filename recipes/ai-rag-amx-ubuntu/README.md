<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Corporation Copyright

**Contributors: William Fowler, Joshua Segovia, Chris Ah-Siong**

# Intel® Gen AI RAG DEMO using Xeon AMX

## Description 

Retrieval Augmented Generation (RAG) is a powerful technique that combines the capabilities of pre-trained Large Language Models (LLMs) with external data sources. 

This application allows users to select a popular large language model, a specific RAG dataset, and query a question to the LLM to showcase an LLM RAG's capability. Users can explore and evaluate the responses of the following models: 

 Models were 

 Mistral OpenOrca FineTune - Chat Based | 7B Parameters | MistralAI Trained | 
 Orca2 - Instruction Based | 13B Parameters | Microsoft Trained | 
 Llama2 - Instruction Based | 13B Parameters | Nous Research Trained | 
 GPT4ALL Snoozy - Instruction Based | 13B Parameters | NomicAI Trained | 

To enhance efficiency, the application leverages Intel Advanced Matrix Extensions Technology (AMX). AMX provides specialized instructions for matrix multiplication, convolution, and linear algebra operations to reduce latency, a crucial aspect for chat based LLMs.

## Usage

[**AWS - Intel® Optimized Cloud Modules for HashiCorp Terraform example**](https://github.com/intel/terraform-intel-aws-vm/tree/fast-rag/examples/gen-ai-rag-demo) 

### Dependencies

## Running the Demo

1. SSH into newly created GCP VM and run `source /usr/local/tmp/optimized-cloud-recipes/recipes/ai-rag-ubuntu/gradio_rag.py`

2. On your computer open a browser and navigate to the Gradio link that is provided on your terminal

Note: Wait around 10-15 minutes for the models to be downloaded before running the demo

## Help

## Authors



## TESTING A COMMIT