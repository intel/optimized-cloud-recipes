#!/bin/bash

public_ip=$(ec2metadata --public-ipv4)
host_ip=$(hostname -I | awk '{print $1}')
export host_ip=$host_ip
export public_ip=$public_ip
export no_proxy=
export http_proxy=
export https_proxy=
export EMBEDDING_MODEL_ID="BAAI/bge-large-en-v1.5"
export RERANK_MODEL_ID="BAAI/bge-reranker-base"
export LLM_MODEL_ID="Intel/neural-chat-7b-v3-3"
export TEI_EMBEDDING_ENDPOINT="http://${host_ip}:6006"
export TEI_RERANKING_ENDPOINT="http://${host_ip}:8808"
export TGI_LLM_ENDPOINT="http://${host_ip}:9009"
export REDIS_URL="redis://${host_ip}:6379"
export INDEX_NAME="rag-redis"
export REDIS_HOST=${host_ip}
export MEGA_SERVICE_HOST_IP=${host_ip}
export EMBEDDING_SERVICE_HOST_IP=${host_ip}
export RETRIEVER_SERVICE_HOST_IP=${host_ip}
export RERANK_SERVICE_HOST_IP=${host_ip}
export LLM_SERVICE_HOST_IP=${host_ip}
export BACKEND_SERVICE_ENDPOINT="http://${public_ip}:8888/v1/chatqna"
export DATAPREP_SERVICE_ENDPOINT="http://${public_ip}:6007/v1/dataprep"
export DATAPREP_GET_FILE_ENDPOINT="http://${public_ip}:6007/v1/dataprep/get_file"
export DATAPREP_DELETE_FILE_ENDPOINT="http://${public_ip}:6007/v1/dataprep/delete_file"
#export HUGGINGFACEHUB_API_TOKEN="YourHuggingfaceToken"
