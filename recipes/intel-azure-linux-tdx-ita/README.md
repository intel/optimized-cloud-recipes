<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Corporation Copyright

# Intel® Optimized Cloud Modules for Ansible

**Contributors: Dave Shrestha*

# Intel®  Azure Linux TDX VM with Intel Trust Autority Attestation (ITA)

## Description 

The purpose of this recipe is to setup requiremetns to configure Intel Trust Authority (ITA) Attestation on an Azure VM that supports Intel Trusted Domain Extensions (TDX)
This recipe works in conjunction with the [Intel Azure Linux TDX ITA terraform module](https://github.com/intel/terraform-intel-azure-linux-vm/tree/main/examples)

## Usage

[**Azure - Intel® Optimized Cloud Modules for HashiCorp Terraform Azure TDX with Intel Trust Autority Attestation**](https://github.com/intel/terraform-intel-azure-linux-vm/tree/ds-terraform-intel-azure-tdx-attestation-linux-vm/examples/azure-linux-tdx-ita-attestation-vm) 

## Verifying TDX
1. Wait 10min after the Intel Azure Linux TDX ITA terraform msodule was excuted to give it time to complete then SSH into newly created VM and issue following command: `sudo dmesg | grep -i tdx`
   NOTE: Make to to assign a Pubilic IP to that VM and ensure the Azure NSG has port 22 Inbound access from your IP

You should see: "Memory Encryption Features active: Intel TDX"

2. cd /trustauthority-client/tdx-cli and cat ITA-Token.tok and you will see massive encrypted text
