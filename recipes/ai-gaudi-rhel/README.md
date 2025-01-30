<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Optimized Cloud Modules for Ansible  - Intel® Gaudi® on Redhat Enterprise Linux

## Overview

| Area   | Description                                                 |
| :----- | :---------------------------------------------------------- |
| Recipe | **Gaudi on Redhat Enterprise Linux** |
Demo | Setups environment to run Gaudi Demos |  [LINK](TBD)
| Install time | 15 minutes |
| Logs | `tail -f /var/log/syslog`|

## Prerequisites

| Optimized for | Description                              |
| :------------ | :--------------------------------------- |
| OS            | Redhat Enterprise Linux* 9.4 or newer               |
| Hardware      | Intel® Gaudi® AI Accelerator |

## Usage

Main usage option:

### Running Ansible manually via the Operating System command line

Pick the recipe file based on the version of the Intel® Gaudi® drivers

| Driver Version | Recipe File | Notes |
| :------------- | :---------- | :---- |
| 1.19.0         | [rhel-baremetal-recipe-1.19.0.yml](rhel-baremetal-recipe-1.19.0.yml)| For clean installs or upgrades. Checks to see if the SPI 
Firmware needs to be upgraded. | 
| 1.19.1         | [rhel-baremetal-recipe-1.19.1.yml](rhel-baremetal-recipe-1.19.1.yml)| For clean installs or upgrades. Checks to see if the SPI 
Firmware needs to be upgraded. |

For example, on RHEL:

```bash
# Install Git 
sudo dnf install git -y

# Install Ansible
sudo dnf install epel-release
sudo dnf install ansible ansible-core 

# Clone the repo
git clone https://github.com/intel/optimized-cloud-recipes.git 

# Run the recipe, pick the recipe version for the Habana version you want
sudo ansible-playbook optimized-cloud-recipes/recipes/ai-gaudi-rhel/rhel-baremetal-recipe-1.19.1.yml

# Logs at 'tail -f 10 /var/log/syslog'
```

## Running the Demo

1. SSH into the host and run:

```bash
sudo podman run -it --runtime=habana -e HABANA_VISIBLE_DEVICES=all -e OMPI_MCA_btl_vader_single_copy_mechanism=none --cap-add=sys_nice --net=host --ipc=host vault.habana.ai/gaudi-docker/1.19.1/rhel9.4/habanalabs/pytorch-installer-2.5.1:latest
```

2. This will launch the pytorch container where the Gaudi demos can be launched.

## Links

[Intel® Gaudi® AI Accelerator](https://www.intel.com/content/www/us/en/products/details/processors/ai-accelerators/gaudi-overview.html)

[Intel® Gaudi® AI Accelerator - Developer Website](https://developer.habana.ai/)
