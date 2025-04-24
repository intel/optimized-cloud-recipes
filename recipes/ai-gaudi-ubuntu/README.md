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

## Usage

There are two main usage options:

### Option 1 - The simplest way to implement the recipe is with Intel Cloud Modules

[**AWS - Intel® Optimized Cloud Modules for HashiCorp Terraform example**](https://github.com/intel/terraform-intel-aws-vm/tree/main/examples/gen-ai-gaudi-demo)

### Option 2 - Running Ansible manually via the Operating System command line

Pick the recipe file based on the version of the Intel® Gaudi® drivers

| Driver Version | Recipe File | Notes |
| :------------- | :---------- | :---- |
| 1.16.0         | [recipe.yml](recipe.yml)| Used in specific demos, works on AWS DL1 instances |
| 1.16.2         | [standalone-recipe-1.16.2.yml](standalone-recipe-1.16.2.yml)| Doesn't upgrade SPI Firmware |
| 1.17.1         | [baremetal-recipe-1.17.1.yml](baremetal-recipe-1.17.1.yml)| For clean installs or upgrades. Upgrades SPI Firmware.|
| 1.18.0         | [baremetal-recipe-1.18.0.yml](baremetal-recipe-1.18.0.yml)| For clean installs or upgrades. Checks to see if the SPI 
Firmware needs to be upgraded. | 
| 1.19.0         | [baremetal-recipe-1.19.0.yml](baremetal-recipe-1.19.0.yml)| For clean installs or upgrades. Checks to see if the SPI 
Firmware needs to be upgraded. | 
| 1.20.0         | [baremetal-recipe-1.20.0.yml](baremetal-recipe-1.20.0.yml)| For clean installs or upgrades. Checks to see if the SPI 
Firmware needs to be upgraded. | 

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

# Clone the repo
git clone https://github.com/intel/optimized-cloud-recipes.git 

# Run the recipe, pick the recipe version for the Habana version you want
sudo ansible-playbook optimized-cloud-recipes/recipes/ai-gaudi-ubuntu/baremetal-recipe-1.20.0.yml

# Logs at 'tail -f 10 /var/log/syslog'
```

## Running the Demo

1. SSH into newly created VM and run:

```bash
sudo docker run -it --runtime=habana -e HABANA_VISIBLE_DEVICES=all -e OMPI_MCA_btl_vader_single_copy_mechanism=none --cap-add=sys_nice --net=host --ipc=host vault.habana.ai/gaudi-docker/1.19.0/ubuntu22.04/habanalabs/pytorch-installer-2.5.1:latest
```

2. This will launch the pytorch container where the Gaudi demos can be launched.

## Links

[Intel® Gaudi® AI Accelerator](https://www.intel.com/content/www/us/en/products/details/processors/ai-accelerators/gaudi-overview.html)

[Intel® Gaudi® AI Accelerator - Developer Website](https://developer.habana.ai/)
