<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Optimized Cloud Modules for Ansible - 4th Gen Xeon(SPR) AMX using Stable Diffusion on Ubuntu

## Overview

| Area   | Description                                                 |
| :----- | :---------------------------------------------------------- |
| Recipe | **4th Gen Xeon(SPR) AMX using Python + Stable Diffusion on Ubuntu** |
| Features| This Recipes configures Ubuntu with Intel OpenVino and deploys/optimizes Stable Diffusion for 4th Gen Xeon(SPR) with AMX accelerator)
Demo details |  [Stable Diffusion](https://huggingface.co/stabilityai/stable-diffusion-2-1)
| Install time | 3 minutes |
| Logs | `tail -f /var/ansible-log`|

## Prerequisites

| Optimized for | Description                              |
| :------------ | :--------------------------------------- |
| OS            | Ubuntu* 22.04 LTS or newer               |
| Accelerator     | Intel® Advanced Matrix Extensions (AMX)  |
| Hardware      | 4th Gen Intel® Xeon® Scalable Processors |

**Note: GCP and AWS SPR VMs are supported**

## Usage

There are two main usage options:

### Option 1 - The simplest way to implement the recipe is with Intel Cloud Modules

[**GCP - Intel® Optimized Cloud Modules for HashiCorp Terraform example**](https://github.com/intel/terraform-intel-gcp-vm/tree/main/examples/gcp-linux-stable-diffusion)

[**AWS - Intel® Optimized Cloud Modules for HashiCorp Terraform example**](https://github.com/intel/terraform-intel-aws-vm/tree/main/examples/gen-ai-stable-diffusion)


### Option 2 - Running Ansible manually via the Operating System command line

By using [ansible-pull](https://docs.ansible.com/ansible/latest/cli/ansible-pull.html), Ansible can run directly on the host.

For example, on Ubuntu:

```bash
# Install Git 
sudo apt install git -y

# Install Ansible Key
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible

# Install Ansible
sudo apt install ansible -y

#Run ansible-pull
sudo ansible-pull -vv -U https://github.com/intel/optimized-cloud-recipes.git recipes/ai-stable_diffusion-amx-ubuntu/recipe.yml

# Logs at 'tail -f 10 /var/ansible-log'
```

## Run the Intel® OpenVino Optimized Demo

**NOTE - Wait ~5 minutes for the software to install**

**1-SSH into newly created GCP VM and run `source /usr/local/bin/run_demo.sh`**

**2-On your computer open a browser and navigate to http://<VM_PLUBLIC_IP>:5000**


## OPTIONAL - Run the default not-optimized demo

**1-SSH into VM and run `source /usr/local/bin/not_optimized_run_demo.sh`**

**2-Browse to port 5001 instead http://<VM_PLUBLIC_IP>:5001**

## Links

[Intel® Advanced Matrix Extensions (AMX)](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html)

[FastChat](https://github.com/lm-sys/FastChat)
