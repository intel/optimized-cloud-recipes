#!/bin/bash

export no_proxy=
export http_proxy=
export https_proxy=
#export LLM_MODEL_ID="codellama/CodeLlama-7b-Instruct-hf"
export LLM_MODEL_ID="Intel/neural-chat-7b-v3-3"
export TGI_LLM_ENDPOINT="http://${host_ip}:8028"
export MEGA_SERVICE_HOST_IP=${host_ip}
export LLM_SERVICE_HOST_IP=${host_ip}
export BACKEND_SERVICE_ENDPOINT="http://${public_ip}:7778/v1/codegen"
#export HUGGINGFACEHUB_API_TOKEN="YourHuggingfaceToken"
# See link for more details https://github.com/opea-project/GenAIExamples/blob/main/CodeGen/docker_compose/intel/cpu/xeon/compose.yaml

