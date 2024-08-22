<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Optimized Cloud Modules for Ansible  - Intel® Gaudi® on Ubuntu

## Overview

| Area   | Description                                                 |
| :----- | :---------------------------------------------------------- |
| Recipe | **Gaudi on Ubuntu** |
Demo | Setups environment to run Gaudi Demos |  [LINK](TBD)
| Install time | 15 minutes |
| Logs | `tail -f /var/log/syslog`|

## Prerequisites

| Optimized for | Description                              |
| :------------ | :--------------------------------------- |
| OS            | Ubuntu* 22.04 LTS or newer               |
| Hardware      | Intel® Gaudi® AI Accelerator |

**Note: Only AWS DL1 Instances are supported**

## Usage

There are two main usage options:

### Option 1 - The simplest way to implement the recipe is with Intel Cloud Modules

[**AWS - Intel® Optimized Cloud Modules for HashiCorp Terraform example**](https://github.com/intel/terraform-intel-aws-vm/tree/main/examples/gen-ai-gaudi-demo)

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
sudo ansible-pull -vv -U https://github.com/intel/optimized-cloud-recipes.git recipes/ai-gaudi-ubuntu/standalone-recipe.yml

# Logs at 'tail -f 10 /var/log/syslog'
```

## Running the Demo

1. SSH into newly created VM and run:

```bash
sudo docker run -it --runtime=habana -e HABANA_VISIBLE_DEVICES=all -e OMPI_MCA_btl_vader_single_copy_mechanism=none --cap-add=sys_nice --net=host --ipc=host vault.habana.ai/gaudi-docker/1.16.0/ubuntu22.04/habanalabs/pytorch-installer-2.2.2:latest
```

2. This will launch the pytorch container where the Gaudi demos can be launched.

## Links

[Intel® Gaudi® AI Accelerator](https://www.intel.com/content/www/us/en/products/details/processors/ai-accelerators/gaudi-overview.html)

[Intel® Gaudi® AI Accelerator - Developer Website](https://developer.habana.ai/)
