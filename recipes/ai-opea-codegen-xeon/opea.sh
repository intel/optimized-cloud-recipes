#!/bin/bash
# Modify the following TAG variable to influcence the docker image tag on compose.yaml 
# https://github.com/opea-project/GenAIExamples/blob/main/CodeGen/docker_compose/intel/cpu/xeon/compose.yaml
export TAG="latest"
host_ip=$(hostname -I | awk '{print $1}') 
export no_proxy=
export http_proxy=
export https_proxy=
export LLM_MODEL_ID="meta-llama/CodeLlama-7b-hf"
export TGI_LLM_ENDPOINT="http://${host_ip}:8028"
export MEGA_SERVICE_HOST_IP=${host_ip}
export LLM_SERVICE_HOST_IP=${host_ip}
export BACKEND_SERVICE_ENDPOINT="http://${host_ip}:7778/v1/codegen"
export host_ip=$host_ip
#export HUGGINGFACEHUB_API_TOKEN="YourHuggingfaceToken"
