<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# OCR - 4th Gen Xeon(SPR) AMX using PyTorch on Ubuntu

## Overview

| Area                  | Description
|:---                   |:---
| Recipe   | **Enables Python, Intel PyTorch Extensions and deploys a small Bert/Restnet50 demo application**
Demo | To run the built-in amx demo, run: `source /usr/local/bin/run_demo.sh`. The included demo is based of our OneAPI Samples and  demonstrates how to perform inference using the ResNet50 and BERT models using the Intel® Extension for PyTorch
Demo details |  [LINK](https://github.com/oneapi-src/oneAPI-samples/blob/master/AI-and-Analytics/Features-and-Functionality/IntelPyTorch_InferenceOptimizations_AMX_BF16_INT8/README.md)
| Install time      | 3 minutes
| Logs | `tail -f /var/ansible-log` & `tail -f 10 /var/log/dpkg.log`

## Prerequisites

| Optimized for | Description                              |
| :------------ | :--------------------------------------- |
| OS            | Ubuntu* 22.04 LTS or newer               |
| Optimizer     | Intel® Advanced Matrix Extensions (AMX)  |
| Hardware      | 4th Gen Intel® Xeon® Scalable Processors |

**Note: GCP and AWS SPR VMs are supported**

## Usage

There are two main usage options:

### Option 1 - The simplest way to implement the recipe is with Intel Cloud Modules

[**Use the existing GCP Intel® Cloud Optimization Modules for HashiCorp Terraform example**](https://github.com/intel/terraform-intel-gcp-vm/tree/main/examples/gcp-linux-with-aikit)


### Option 2 - Running Ansible manually via the Operating System command line

By using [ansible-pull](https://docs.ansible.com/ansible/latest/cli/ansible-pull.html), Ansible can run directly on the host.

For example, on Ubuntu:

```bash
# Install Git 
sudo apt install git -y

# Install Ansible Key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
sudo apt update

# Install Ansible
sudo apt install ansible -y

#Run ansible-pull
sudo ansible-pull -vvv -U https://github.com/intel/optimized-cloud-recipes.git recipes/ai-pytorch-amx-ubuntu/recipe.yml

# Logs at 'tail -f 10 /var/ansible-log' & 'tail -f 10 /var/log/dpkg.log'
```

### Demo - Execute on the command line: `source /usr/local/bin/run_demo.sh`

## Links

[Intel® OpenAPI Base Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html#gs.3tswe8)

[Intel® OpenAPI AI Analytics Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/ai-analytics-toolkit.html#gs.3tsgs4)

[Intel® Advanced Matrix Extensions (AMX)](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html)
