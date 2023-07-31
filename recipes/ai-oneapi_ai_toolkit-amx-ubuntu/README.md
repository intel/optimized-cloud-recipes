# OCR: OneAPI Base & AI Analytics Toolkit

The OneAPI Base & AI Analytics Toolkit is a set of libraries and tools for developing, training, and deploying high-performance, data analytics, AI and machine learning applications.

## Overview

| Area                  | Description
|:---                   |:---
| Recipe   | **This Optimized Cloud Recipe(OCR) enables the OneAPI Base & AI Analytics Toolkit and deploys a small Bert/Restnet50 demo application**
Demo | The included demo is based off our OneAPI Samples and  demonstrates how to perform inference using the ResNet50 and BERT models using the Intel® Extension for PyTorch
Demo details |  [LINK](https://github.com/oneapi-src/oneAPI-samples/blob/master/AI-and-Analytics/Features-and-Functionality/IntelPyTorch_InferenceOptimizations_AMX_BF16_INT8/README.md)
| Install time      | 30-45 minutes
| Logs | `tail -f /var/ansible-log` & `tail -f 10 /var/log/dpkg.log`

## Prerequisites

| Optimized for | Description                              |
| :------------ | :--------------------------------------- |
| OS            | Ubuntu* 22.04 LTS or newer               |
| Optimizer     | Intel® Advanced Matrix Extensions (AMX)  |
| Hardware      | 4th Gen Intel® Xeon® Scalable Processors |

**Note: GCP and AWS SPR VMs are supported**

## Usage

There are two main usage options:

A. Option 1 - Via a Cloud-init Integration with Intel® Cloud Optimization Modules for HashiCorp Terraform
B. Option 2 - By running Ansible via the command line
C. To run the built-in amx demo, run: `source /usr/local/bin/run_demo.sh`

### Option 1 - Integration with Intel® Cloud Optimization Modules for HashiCorp Terraform via Cloud-Init

Overview:
You can run this playbook by using  [Intel® Cloud Optimization Modules for Terraform](https://github.com/intel/terraform-intel-gcp-vm/tree/main/examples/gcp-linux-with-aikit), or by using Ansible or [Ansible Pull](https://docs.ansible.com/ansible/latest/cli/ansible-pull.html) on an Ubuntu system.

If you already have a VM provisioned, you can run `ansible-pull -U https://github.com/intel/optimized-cloud-recipes.git recipes/ai-oneapi_ai_toolkit-amx-ubuntu/recipe.yml`

It takes about 30 minutes for everything to run (mainly the intel-aikit install). You can check if the install is complete by running cat /var/ansible-log and checking if the task “Reboot server” has run. 

 
1. The following demonstrates how to use the `ai-oneapi_ai_toolkit-amx-ubuntu` recipe with the Intel GCP module for Terraform. [GCP Module example link](https://github.com/intel/terraform-intel-gcp-vm/tree/main/examples/gcp-linux-with-aikit).
2. It uses the Terraform `user_data` argument that enables the execution on the `cloud_init.yml` file.
3. The `cloud_init.yml` file calls the Ansible playbook that installs the recipe by calling the `recipe.yml` file directly from Github.

Example:

```hcl
# main.tf Terraform file that deploys GCP VM via the GCP VM Module

# Cloud-init file that calls Ansible playbook, see 'user_data' below
data "template_file" "user_data" {
  template = file("./cloud_init.yml")
}

# GCP VM Module
module "linux_vm" {
  source              = "intel/gcp-vm/intel"
  project             = "123456789"
  boot_image_project  = "ubuntu-os-cloud"
  boot_image_family   = "ubuntu-2204-lts"
  name                = "gcp-linux-with-aikit"
  zone                = "us-central1-a" 
  access_config = [{
    nat_ip                 = null
    public_ptr_domain_name = null
    network_tier           = "PREMIUM"
  }, ]
  # Integration between Terraform and Cloud-init
  user_data    = data.template_file.user_data.rendered 
}
```

```yaml
# Cloud-init file that calls Ansible playbook
package_update: true
package_upgrade: true

package:
  - git

ansible:
  install_method: distro
  package_name: ansible
  pull:
    url: "https://github.com/intel/optimized-cloud-recipes.git"
    playbook_name: "recipes/ai-oneapi_ai_toolkit-amx-ubuntu/recipe.yml"
```

### Option 2 - Running Ansible via the Operating System command line

Follow Ansible installation procedures for your operating system

<https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html>

For example, on Ubuntu:

```bash
# Install Ansible Key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
sudo apt update

# Install Git and clone this repository
sudo apt install git -y
git clone https://github.com/intel/optimized-cloud-recipes.git

# Install Ansible and run the recipe
sudo apt install ansible -y
sudo ansible-playbook ./optimized-cloud-recipes/recipes/ai-oneapi_ai_toolkit-amx-ubuntu/recipe.yml
```

## Links

[Intel® OpenAPI Base Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html#gs.3tswe8)

[Intel® OpenAPI AI Analytics Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/ai-analytics-toolkit.html#gs.3tsgs4)

[Intel® Advanced Matrix Extensions (AMX)](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html)
