
<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Optimized Cloud Recipes (OCRs)

© Copyright 2023, Intel Corporation

## Overview


**Intel® Optimized Cloud Recipes (OCRs) are:**

1. A combination of documentation(markdown) and scripted automation.
2. Developed to enable/optimize technologies on Intel® Architecture (IA).
3. Scripts that **depend** on existing Intel® Tuning Guides that were generated from testing and benchmarking exercises.
4. Currently focused on enabling Infrastructure-as-a-Service (IaaS) Virtual Machines (VMs) on public cloud providers (today, on-prem hardware configuration is not supported).
5. Written in Ansible or PowerShell, meant to automate operating system and above configuration.
6. Ready to be Integrated into Intel® Cloud Optimization Modules for HashiCorp Terraform using Cloud Cloud-Init integration. See [GCP Module example](https://github.com/intel/terraform-intel-gcp-vm/tree/main/examples/gcp-linux-with-aikit)).
7. Can also be used directly on their own(see usage on each recipe).

**Currently out-of-scope for OCRs:**

1. Physical on-prem hardware configuration.
2. Defining tuning parameters/knobs and values that are required to optimize a workload.
3. Benchmarking.



**Note: OCRs focus on the enablement of Intel Technologies and often will include a demo but are not meant to be a benchmarking tool.**

**Intel is working on a separate benchmarking repository called [Workload Services Framework](https://github.com/intel/workload-services-framework) that will consume these recipes and provide benchmarking capabilities.**


## Value

The primary goal of OCRs is to simplify and accelerate the enablement of Intel® Technologies on public cloud VMs.

## Examples of Recipes

Some examples of technologies that can be enabled and optimized are:

- OneAPI AI Training and Inference with Intel® Advanced Matrix Extensions (Intel® AMX)
- Encryption/Decryption with Intel Quick Assist Technology (Intel QAT)
- MySQL Open Source Database
- PostgreSQL Open Source Database

## Intel® Cloud Optimization Modules for HashiCorp, the OCRs companion

The Intel® Cloud Optimization Modules for HashiCorp Terraform enable the deployment of optimized instances on public cloud. The modules are available on the [Terraform Registry](https://registry.terraform.io/modules/intel).

**The Modules can be easily integrated with these Recipes, see Usage below.**

## Usage

Recipes are located in the `./recipes` folder. Each recipe has its own folder and contains a `README.md` file with instructions on how to use it.

There are two primary ways to use these Recipes:

1. **Via a Cloud-init Integration with Intel® Cloud Optimization Modules for HashiCorp Terraform**
2. **By running Ansible via the command line**

### Option 1 - Integration with Intel® Cloud Optimization Modules for HashiCorp Terraform via Cloud-Init

Overview:

1. The following demonstrates how to use the `ai-pytorch-amx-ubuntu` recipe with the Intel GCP module for Terraform.
2. It uses the Terraform `user_data` argument that enables the execution on the `cloud_init.yml` file.
3. The `cloud_init.yml` file calls the Ansible playbook that installs the recipe by calling the `recipe.yml` file directly from Github.

[GCP Module example link](https://github.com/intel/terraform-intel-gcp-vm/tree/main/examples/gcp-linux-with-aikit)

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
    playbook_name: "recipes/ai-pytorch-amx-ubuntu/recipe.yml"
```

### Option 2 - Running Ansible via the Operating System command line

Follow Ansible installation procedures for your operating system

<https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html>

For example, on Ubuntu by using [ansible-pull](https://docs.ansible.com/ansible/latest/cli/ansible-pull.html), Ansible can run directly on the host:

```bash
# Install Git 
sudo apt install git -y

# Install Ansible Key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
sudo apt update

# Install Ansible
sudo apt install ansible -y

#Run ansible-pull
sudo ansible-pull -vv -U https://github.com/intel/optimized-cloud-recipes.git recipes/ai-pytorch-amx-ubuntu/recipe.yml

# Logs at 'tail -f 10 /var/ansible-log' & 'tail -f 10 /var/log/dpkg.log'
```

## Repo Structure

The repository structure is very simple. All recipes will be located under the `./recipes` folder.

The recipes folders are structured as `<category>-<workload name>-<intel tech enabled>-<OS>`

Categories are: ai, compute, data, media, ml, networking

Examples:

- ai-pytorch-amx-ubuntu
- networking-java-qat-ubuntu
- database-mysql-avx512-ubuntu
- database-mssql-qat-windows


## Integrations with Intel® Cloud Optimization Modules for HashiCorp Terraform

See Usage -> Option 1 above

A diagram showcasing the integration is coming!


## Development Environment

We recommend using a Linux environment. If on Windows, we [recommend using WSL2](https://learn.microsoft.com/en-us/windows/wsl/install).

You will only need git and Ansible installed on your development environment. Follow Ansible installation procedures for your operating system. <https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html>

For example, on Ubuntu:

```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
sudo apt update
sudo apt install git -y
sudo apt install ansible -y
```

Note: *If you are an Intel® employee, reach out to the Repository Owners. We have additional environment configuration information that can help you.*

## How to contribute

Please see [CONTRIBUTING.md](https://github.com/intel/optimized-cloud-recipes/blob/main/CONTRIBUTING.md)

We are glad to review and accept contributions.

## Considerations

Today, the scope is limited to enabling/optimizing VMs on public cloud providers.

The OCRs are currently not managing on-prem physical hardware configurations.
