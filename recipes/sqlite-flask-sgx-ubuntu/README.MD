<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# OCR - 3rd Gen Xeon(ICX) SGX using Gramine on Ubuntu

## Overview

| Area                  | Description
|:---                   |:---
| Recipe   | **Enables SGX, Gramine, and setups flask-sqlite demo for SGX**
Demo | To run the choose one of the Usage options below
Demo details |  [LINK](https://github.com/intel/terraform-intel-azure-linux-vm/blob/main/examples/azure-linux-vm-sgx-gramine-recipe-example/README.md)
| Install time      | 5 minutes
| Logs | `tail -f /var/ansible-log` &  `tail -f 10 /tmp/contrib/Intel-Confidential-Compute-for-X/workloads/flask/sgx-app.log`

## Prerequisites

| Optimized for | Description                              |
| :------------ | :--------------------------------------- |
| OS            | Ubuntu* 20.04 LTS or newer               |
| Optimizer     | Intel® Software Guard Extensions (SGX)  |
| Hardware      | 3rd Gen Intel® Xeon® Scalable Processors |

**Note: Intel SGX Capable Host available on Azure**

## Usage

There are two main usage options:

### Option 1 - The simplest way to implement the recipe is with Intel Cloud Modules

[**Use the existing Azure Intel® Cloud Optimization Modules for HashiCorp Terraform example**](https://github.com/intel/terraform-intel-azure-linux-vm/tree/main/examples/azure-linux-vm-sgx-gramine-recipe-example)


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
sudo ansible-pull -vvv -U https://github.com/intel/optimized-cloud-recipes.git recipes/sqlite-flask-sgx-ubuntu/gramine-recipe.yml

# Follow the instructions here to run the demo : https://github.com/intel/terraform-intel-azure-linux-vm/blob/main/examples/azure-linux-vm-sgx-gramine-recipe-example/README.md

# Logs at `tail -f /var/ansible-log` &  `tail -f 10 /tmp/contrib/Intel-Confidential-Compute-for-X/workloads/flask/sgx-app.log`
```

## Links
