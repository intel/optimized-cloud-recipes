# Overview
This demo demonstrates the speedup in Large Language Model CPU inference from 3rd gen Xeon to 4th gen Xeon. It uses [FastChat](https://github.com/lm-sys/FastChat) to serve the 3B parameter fastchat-t5 model.

# Running the Recipe
The easiest way to run this recipe is using [Intel® Cloud Optimization Modules for Terraform](https://github.com/intel/terraform-intel-gcp-vm/tree/main/examples/gcp-linux-fastchat)

# Running the Demo
SSH into your VM from the cloud console. Wait for a few minutes to ensure that the recipe has run completely. 

Ssh into the c3 instance and run

`python3 -m fastchat.serve.gradio_web_server_multi --share` 
=======
<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# OCR - 4th Gen Xeon(SPR) AMX using Python + FastChat on Ubuntu

## Overview

| Area   | Description                                                 |
| :----- | :---------------------------------------------------------- |
| Recipe | **4th Gen Xeon(SPR) AMX using Python + FastChat on Ubuntu** |
Demo | **SSH and run: `source /usr/local/bin/run_demo.sh` then on your computer open a browser and navigate to a public gradio link or open port 7860 and navigate to http://<VM_PLUBLIC_IP>:7860.** This demo demonstrates Large Language Model CPU inference using 4th Gen Xeon(SPR). It uses [FastChat](https://github.com/lm-sys/FastChat) to serve the 3B parameter fastchat-t5 model. **NOTE: If you do not want to proxy data through https://xxxxxxxxxxxx.gradio.live, this demo requires port 7860 to be open for the VM.**
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

## Running the Demo


Otherwise, if you choose to open port 7860 in main.tf: on your computer, open a browser and navigate to http://<VM_PLUBLIC_IP>:7860. Get your Public IP from the "Compute Engine" section of the GCP console.

**1-SSH into newly created GCP VM and run `source /usr/local/bin/run_demo.sh`**

**2-On your computer open a browser and navigate to https://xxxxxxx.gradio.live OR http://<VM_PLUBLIC_IP>:7860**

NOTE: You can use the proxy the Gradio proxy https://xxxxxxx.gradio.live URL that is generated during the gradio run(see console output).

Otherwise, this demo requires port 7860 to be open. If you are running this on GCP, you will need to open this port in the GCP Firewall Policies. If you are running this on AWS, you will need to open this port in the AWS security group.

--- KNOWN ISSUE ---

This may fail. In this case, run

`pip install gradio==3.10`
`pip install gradio==3.35.2`

Then, run:
`python3 -m fastchat.serve.gradio_web_server_multi --share` 

and go to the gradio link

 
=======
`source /usr/local/bin/run_demo.sh` 

and navigate to the public gradio link, or open port 7860 and navigate to http://<VM_PLUBLIC_IP>:7860 on your computer.

## Links

[Intel® Advanced Matrix Extensions (AMX)](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html)

[FastChat](https://github.com/lm-sys/FastChat)
