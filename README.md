
<p align="center">
  <img src="./images/logo-classicblue-800px.png" alt="Intel Logo" width="250"/>
</p>

### WORK IN PROGRESS

# Intel® Optimized Cloud Recipes (OCRs)

© Copyright 2023, Intel Corporation

## Overview


Intel® Optimized Cloud Recipes (OCRs) are:

1. A combination of documentation(markdown) and scripted automation developed to enable/optimize technologies on Intel® Architecture (IA)
2. Currently focused on enabling Infrastructure-as-a-Service(IaaS) Virtual Machines(VMs) on public cloud providers (today, no hardware configuration is supported)
3. Written in Ansible or PowerShell, meant to automate operating system and above configuration
4. Ready to be Integrated into Intel® Cloud Optimization Modules for HashiCorp Terraform using Cloud Cloud-Init integration ([GCP Module example](https://github.com/intel/terraform-intel-gcp-vm/tree/main/examples/gcp-linux-with-aikit))
5. Or used directly on their own(see usage on each recipe)

## Examples of Recipes

Some example of technologies that can be enabled and optimized are:

- AI Training and Inference with Intel® Advanced Matrix Extensions (Intel® AMX)
- Encryption/Decryption with Intel Quick Assist Technology (Intel QAT)
- MySQL Open Source Database
- PostgreSQL Open Source Database

## Intel Cloud Optimization Modules

The Intel® Cloud Optimization Modules for HashiCorp Terraform are a set of modules that enable the deployment of optimized instances on public cloud providers. The modules are available on the [Terraform Registry](https://registry.terraform.io/modules/intel).

These modules can be easily integrated with these Recipes, see **Usage** below.

## Usage

Recipes are located in the `./recipes` folder. Each recipe has its own folder and contains a `README.md` file with instructions on how to use it.

There are two primary ways to use these Recipes:

1. Via a Cloud-init Integration with Intel® Cloud Optimization Modules for HashiCorp Terraform
2. By running Ansible via the command line

### Option 1 - Integration with Intel® Cloud Optimization Modules for HashiCorp Terraform via Cloud-Init

Overview:

1. The following demonstrates how to use the `ai-oneapi_ai_toolkit-amx-ubuntu` recipe with the Intel GCP module for Terraform.
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

## Repo Structure

The repository structure is very simple. All recipes will be located under the `./recipes` folder.

The recipes folders are structured as `<category>-<workload name>-<intel tech enabled>-<OS>`

Categories are: ai, compute, data, media, ml, networking

Examples:

- ai-oneapi_ai_toolkit-amx-ubuntu
- networking-java-qat-ubuntu
- database-mysql-avx512-ubuntu
- database-mssql-qat-windows


## Integrations with Intel® Cloud Optimization Modules for HashiCorp Terraform

See Usage -> Option 1 above

A diagram showcasing the integration is coming!


## Development Environment

We recommend using a Linux environment. If on Windows, we [recommend using WSL2](https://learn.microsoft.com/en-us/windows/wsl/install).

You will only need git and ansible installed on your development environment. Follow Ansible installation procedures for your operating system. <https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html>

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

We are currently not managing physical hardware configurations.
