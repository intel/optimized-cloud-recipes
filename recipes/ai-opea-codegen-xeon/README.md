<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Optimized Cloud Modules for Ansible - OPEA CodeGen Example on Intel® Xeon®

## Overview

| Area   | Description                                                 | Links |
| :----- | :---------------------------------------------------------- | :-------- |
| Recipe | **OPEA CodeGen on Intel® Xeon® on Ubuntu** ||
Demo | OPEA CodeGen on Intel® Xeon® |  [OPEA CodeGen](https://github.com/opea-project/GenAIExamples/tree/main/CodeGen/docker_compose/intel/cpu/xeon) |
| Install time | 15 minutes | |
| Logs | `tail -f /var/log/cloud-init-output.log`| |

## Prerequisites

| Optimized for | Description                              |
| :------------ | :--------------------------------------- |
| OS            | Ubuntu* 22.04 LTS or newer               |
| Hardware      | Intel® Xeon® with Intel® Advanced Matrix Extensions |

**A number of ports need to be opened for this to work correctly, refer to the [OPEA example](https://github.com/opea-project/GenAIExamples/tree/main/CodeGen/docker_compose/intel/cpu/xeon) for details.**

## Usage

There are two main usage options:

### Option 1 - The simplest way to implement the recipe is with Intel Cloud Modules

[**AWS - Intel® Optimized Cloud Modules for HashiCorp Terraform example**](https://github.com/intel/terraform-intel-aws-vm/tree/main/examples/gen-ai-xeon-opea-codegen)

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

# Clone the repo
git clone https://github.com/intel/optimized-cloud-recipes.git

# Modify the opea.sh file and set the `host_ip` variable to your host's IP and uncomment and set your Huggingface Token, then source the opea.sh file
nano recipes/ai-opea-codegen-xeon/opea.sh
source recipes/ai-opea-codegen-xeon/opea.sh

# Run the recipe
sudo ansible-playbook recipes/ai-opea-codegen-xeon/recipe.yml

# Logs at 'tail -f 10 /var/log/syslog'
```

## Accessing the demo

1. Open a browser and go to 'http://yourpublicip:5173'

2. This will launch the UI for the demo.

## Tips

### Changing the models used

To change the models or to troubleshoot, stop the containers by running the following:

```bash

sudo bash
cd /opt/GenAIExamples/CodeGen/docker_compose/intel/cpu/xeon

# Stop the containers
docker compose -f compose.yaml down

# Modify the /etc/profile.d/opea.sh with the new Models
nano /etc/profile.d/opea.sh

# Source the new file
. /etc/profile.d/opea.sh

# Restart the containers
docker compose -f compose.yaml up -d

```

### Troubleshooting the Ansible Playbook  

If the Ansible playbook fails, you can troubleshoot by running the following:

```bash

sudo bash
cd /tmp/optimized-cloud-recipes/recipes/ai-opea-codegen-xeon
cp opea.sh /etc/profile.d/opea.sh
# Enter your HuggingFace Token in the command below
echo 'export HUGGINGFACEHUB_API_TOKEN=${HUGGINGFACEHUB_API_TOKEN}' | sudo tee -a /etc/profile.d/opea.sh
chmod +x /etc/profile.d/opea.sh
. /etc/profile.d/opea.sh
ansible-playbook recipe.yml

```

### Add HuggingFace Token

The Intel® Optimized Cloud Modules for HashiCorp Terraform that leverages this recipe will insert the user's HuggingFace token, if this demo is run manually, make sure to `export HUGGINGFACEHUB_API_TOKEN=yourtoken`. If the containers are running, stop them, export the token and then restart the containers.

## Links

[Intel® Advanced Matrix Extensions](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html)

[Open Platform for Enterprise AI](https://opea.dev/)
