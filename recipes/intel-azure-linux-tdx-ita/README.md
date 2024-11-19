<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Corporation Copyright

# Intel® Optimized Cloud Modules for Ansible

**Contributors: Dave Shrestha*

# Intel®  Azure Linux TDX VM with Intel Trust Autority Attestation (ITA)

## Description 

The purpose of this recipe is to setup all Intel Trust Authority (ITA) Attestation on an Azure VM that supports Intel Trusted Domain Extensions (TDX): This reccipe installs all Intel Trust Authority (ITA) client and its CLI with your ITA Token (you will need to add your ITA token in the ita-recipe.yml file). 



## Usage

[**Azure - Intel® Optimized Cloud Modules for HashiCorp Terraform Azure TDX with Intel Trust Autority Attestation**](https://github.com/intel/terraform-intel-azure-linux-vm/tree/ds-terraform-intel-azure-tdx-attestation-linux-vm/examples/azure-linux-tdx-ita-attestation-vm) 

## Verifying TDX
1. SSH into newly created VM and issue following command: `sudo dmesg | grep -i tdx`

You should see: "Memory Encryption Features active: Intel TDX"

