<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Optimized Cloud Modules for Ansible - 4th Gen Xeon(SPR) AMX on Ubuntu  

## Overview

| Area                  | Description
|:---                   |:---
| Recipe   | **Runs Stable Diffusion with the Easy Diffusion Web UI**
Demo | Simply run the ansible playbook and ensure port 9000 is open
Demo details |  [Easy Diffusion](https://github.com/easydiffusion/easydiffusion)
| Install time      | 5 - 10 minutes
| Logs | `tail -f /var/ansible-log` & `tail -f 10 /var/log/dpkg.log`

## Prerequisites

| Optimized for | Description                              |
| :------------ | :--------------------------------------- |
| OS            | Ubuntu* 22.04 LTS or newer               |
| Optimizer     | Intel® Advanced Matrix Extensions (AMX)  |
| Hardware      | 4th Gen Intel® Xeon® Scalable Processors |

**Note: GCP C3 & AWS m7i VMs are supported**

## Usage

There are two main usage options:

### Option 1 - The simplest way to use the recipe is with Intel Cloud Modules

[**Use the existing GCP Intel® Cloud Optimization Modules for HashiCorp Terraform example**](https://github.com/intel/terraform-intel-gcp-vm/tree/main/examples/gcp-linux-stable-diffusion/)

This automatically provisions the correct VM, OS and firewall rules on GCP

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
sudo ansible-pull -vvv -U https://github.com/intel/optimized-cloud-recipes.git recipes/ai-pytorch-amx-ubuntu/recipe.yml

# Logs at 'tail -f 10 /var/ansible-log' & 'tail -f 10 /var/log/dpkg.log'
```

### Demo - The demo will be accessible at <HOST IP>:9000, e.g. 99.999.999.999:9000

## Links

[Intel® OpenAPI Base Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html#gs.3tswe8)

[Intel® OpenAPI AI Analytics Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/ai-analytics-toolkit.html#gs.3tsgs4)

[Intel® Advanced Matrix Extensions (AMX)](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html)
