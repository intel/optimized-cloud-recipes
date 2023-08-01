# OCR: OneAPI Base & AI Analytics Toolkit

The OneAPI Base & AI Analytics Toolkit is a set of libraries and tools for developing, training, and deploying high-performance, data analytics, AI and machine learning applications.

## Overview

| Area                  | Description
|:---                   |:---
| Recipe   | **This Optimized Cloud Recipe(OCR) enables the OneAPI Base & AI Analytics Toolkit and deploys a small Bert/Restnet50 demo application**
Demo | To run the built-in amx demo, run: `source /usr/local/bin/run_demo.sh`. The included demo is based off our OneAPI Samples and  demonstrates how to perform inference using the ResNet50 and BERT models using the Intel® Extension for PyTorch
Demo details |  [LINK](https://github.com/oneapi-src/oneAPI-samples/blob/master/AI-and-Analytics/Features-and-Functionality/IntelPyTorch_InferenceOptimizations_AMX_BF16_INT8/README.md)
| Install time      | 30-45 minutes
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

- Option 1 - Via a Cloud-init Integration with Intel® Cloud Optimization Modules for HashiCorp Terraform
- Option 2 - By running Ansible via the command line
- To run the built-in amx demo, run: `source /usr/local/bin/run_demo.sh`

### Option 1 - Integration with Intel® Cloud Optimization Modules for HashiCorp Terraform via Cloud-Init

**Use the existing [GCP Module example link](https://github.com/intel/terraform-intel-gcp-vm/tree/main/examples/gcp-linux-with-aikit).**

Details:

1. The following demonstrates how to use the `ai-oneapi_ai_toolkit-amx-ubuntu` recipe with the Intel GCP module for Terraform. 
2. It uses the Terraform `user_data` argument that enables the execution on the `cloud_init.yml` file.
3. The `cloud_init.yml` file calls the Ansible playbook that installs the recipe by calling the `recipe.yml` file directly from Github.

### Option 2 - Running Ansible via the Operating System command line

By using [ansible-pull](https://docs.ansible.com/ansible/latest/cli/ansible-pull.html), Ansible can run directly on the host.

For example, on Ubuntu:

```bash
# Install Git
sudo apt install git -y

# Install Ansible and run the recipe
sudo apt install ansible -y
sudo ansible-pull -U https://github.com/intel/optimized-cloud-recipes.git recipes/ai-oneapi_ai_toolkit-amx-ubuntu/recipe.yml
```

## Links

[Intel® OpenAPI Base Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html#gs.3tswe8)

[Intel® OpenAPI AI Analytics Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/ai-analytics-toolkit.html#gs.3tsgs4)

[Intel® Advanced Matrix Extensions (AMX)](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html)
