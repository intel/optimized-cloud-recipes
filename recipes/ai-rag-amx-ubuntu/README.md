<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Corporation Copyright

**Contributors: William Fowler, Joshua Segovia, Chris Ah-Siong**

# Intel® Gen AI RAG DEMO using Xeon AMX

## Description 

The purpose of this demo aims to demonstrate the powerful capabilities of retrieval augmented generation based on large language models deployed on an Intel Xeon AWS instance (M7i.8xlarge), where we highlight performance optimizations leveraging Intel instructions to deliver increased accuracy and speed of inference. 

The demo consists of a chatbot, that utilizes a combination of LLMs and RAG to generate responses to user queries. The core of the chatbot’s response generation lies in the different LLMs being used:  

## Non-Intel Trained
Mistral OpenOrca FineTune - Chat Based | 7B Parameters | MistralAI Trained |

Orca2 - Instruction Based | 13B Parameters | Microsoft Trained |

Llama2 - Instruction Based | 13B Parameters | Nous Research Trained |

GPT4ALL Snoozy - Instruction Based | 13B Parameters | NomicAI Trained |

## Intel Trained: 
Intel Neural Chat - Chat Based | 7B Parameters | Intel Fine-Tuned

##

In particular, the non-intel models utilize AVX instructions, enhancing computational efficiency for real time information retrieval. The intel trained neural chat model further benefits from AMX, providing additional performance improvements for handling complex matrix operations. These optimizations enable users to perform inference without the need for specialized hardware and can deliver high-quality results efficiently on Intel Xeon CPUs. 

Additionally, we implement RAG with LangChain, which retrieves relevant context or passages from the datasets (ranging from robot maintenance to minor healthcare consultations). The chatbot then utilizes the LLM to generate contextually relevant responses based on both the retrieved context, and the user query. 

https://gpt4all.io/index.html

## Usage

[**AWS - Intel® Optimized Cloud Modules for HashiCorp Terraform example**](https://github.com/intel/terraform-intel-aws-vm/tree/fast-rag/examples/gen-ai-rag-demo) 

## Running the Demo

1. SSH into newly created AWS VM and run `source /usr/local/tmp/optimized-cloud-recipes/recipes/ai-rag-ubuntu/gradio_rag.py`

2. On your computer open a browser and navigate to the Gradio link that is provided on your terminal

Note: Wait around 10-15 minutes for the models to be downloaded before running the demo