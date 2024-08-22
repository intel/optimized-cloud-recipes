<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Optimized Cloud Modules for Ansible - OPEA ChatQnA Example on Intel® Xeon®

## Overview

| Area   | Description                                                 | Links |
| :----- | :---------------------------------------------------------- | :-------- |
| Recipe | **OPEA ChatQnA on Intel® Xeon® on Ubuntu** ||
Demo | OPEA ChatQnA on Intel® Xeon® |  [OPEA ChatQnA](https://github.com/opea-project/GenAIExamples/tree/main/ChatQnA/docker/xeon) |
| Install time | 15 minutes | |
| Logs | `tail -f /var/log/cloud-init-output.log`| |

## Prerequisites

| Optimized for | Description                              |
| :------------ | :--------------------------------------- |
| OS            | Ubuntu* 22.04 LTS or newer               |
| Hardware      | Intel® Xeon® with Intel® Advanced Matrix Extensions |

**A number of ports need to be opened for this to work correctly, refer to the [OPEA example](https://github.com/opea-project/GenAIExamples/tree/main/ChatQnA/docker/xeon) for details.**

## Usage

There are two main usage options:

### Option 1 - The simplest way to implement the recipe is with Intel Cloud Modules

[**AWS - Intel® Optimized Cloud Modules for HashiCorp Terraform example**](https://github.com/intel/terraform-intel-aws-vm/tree/main/examples/gen-ai-xeon-opea-demo)

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
sudo ansible-pull -vv -U https://github.com/intel/optimized-cloud-recipes.git recipes/ai-apea-chatqna-xeon/recipe.yml

# Logs at 'tail -f 10 /var/log/syslog'
```

## Accessing the demo

1. Open a browser and go to 'http://yourpublicip:5174'

2. This will launch the UI for the demo.

## Tips

### Changing the models used

To change the models, stop the containers by running the following:

`docker compose -f /opt/GenAIExamples/ChatQnA/docker/xeon/docker_compose.yaml down`

Modify the file `/etc/profile.d/opea.sh` to change the models used. After making the changes you want, re-source the environment variables by running:

`source /etc/profile.d/opea.sh`

Then relaunch the containers with:

`docker compose -f /opt/GenAIExamples/ChatQnA/docker/xeon/docker_compose.yaml up -d`

### Running the example outside of AWS

To run this example outside of AWS you will need to modify the `opea.sh` file to update the line with `host_ip=$(ec2metadata --public-ipv4)` to `host_ip=youripaddress`

### Add HuggingFace Token

The Intel® Optimized Cloud Modules for HashiCorp Terraform that leverages this recipe will insert the user's HuggingFace token, if this demo is run manually, make sure to `export HUGGINGFACEHUB_API_TOKEN=yourtoken`. If the containers are running, stop them, export the token and then restart the containers.

## Links

[Intel® Advanced Matrix Extensions](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html)

[Open Platform for Enterprise AI](https://opea.dev/)
