<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# OCR - 4th Gen Xeon(SPR) AMX using Python + FastChat on Ubuntu

## Overview



| Area   | Description                                                 |
| :----- | :---------------------------------------------------------- |
| Recipe | **4th Gen Xeon(SPR) AMX using Python + FastChat on Ubuntu** |
Demo | SSH and run: `source /usr/local/bin/run_demo.sh` . This demo demonstrates Large Language Model CPU inference using 4th Gen Xeon(SPR). It uses [FastChat](https://github.com/lm-sys/FastChat) to serve the 3B parameter fastchat-t5 model.
Demo details |  [LINK](https://github.com/lm-sys/FastChat)
| Install time | 3 minutes |
| Logs | `tail -f /var/ansible-log`|

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

[**Use the existing GCP Intel® Cloud Optimization Modules for HashiCorp Terraform example**](https://github.com/intel/terraform-intel-gcp-vm/tree/main/examples/gcp-linux-fastchat)


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
sudo ansible-pull -vvv -U https://github.com/intel/optimized-cloud-recipes.git recipes/ai-fastchat-amx-ubuntu/recipe.yml

# Logs at 'tail -f 10 /var/ansible-log'
```

### Demo - Execute on the command line: `source /usr/local/bin/run_demo.sh`

--- KNOWN ISSUE ---

This may fail. In this case, run

`pip install gradio==3.10`
`pip install gradio==3.35.2`

Then, run:

`source /usr/local/bin/run_demo.sh` 

and go to the gradio link in your browser.

## Links

[Intel® Advanced Matrix Extensions (AMX)](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html)

[FastChat](https://github.com/lm-sys/FastChat)