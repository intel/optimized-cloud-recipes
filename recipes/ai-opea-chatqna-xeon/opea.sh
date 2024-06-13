#!/bin/bash
export http_proxy=
export https_proxy=
export EMBEDDING_MODEL_ID="BAAI/bge-base-en-v1.5"
export RERANK_MODEL_ID="BAAI/bge-reranker-large"
export LLM_MODEL_ID="Intel/neural-chat-7b-v3-3"
export TEI_EMBEDDING_ENDPOINT="http://${public_ip}:8090"
export TEI_RERANKING_ENDPOINT="http://${public_ip}:8808"
export TGI_LLM_ENDPOINT="http://${public_ip}:8008"
export REDIS_URL="redis://${public_ip}:6379"
export INDEX_NAME="rag-redis"
export HUGGINGFACEHUB_API_TOKEN=${HUGGINGFACEHUB_API_TOKEN}
export MEGA_SERVICE_HOST_IP=${public_ip}
export EMBEDDING_SERVICE_HOST_IP=${public_ip}
export RETRIEVER_SERVICE_HOST_IP=${public_ip}
export RERANK_SERVICE_HOST_IP=${public_ip}
export LLM_SERVICE_HOST_IP=${public_ip}
export BACKEND_SERVICE_ENDPOINT="http://${public_ip}:8888/v1/chatqna"