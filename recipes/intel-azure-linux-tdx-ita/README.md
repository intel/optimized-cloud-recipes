<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Corporation Copyright

# Intel® Optimized Cloud Modules for Ansible

**Contributors: Dave Shrestha*

# Intel® TDX WITH Intel Trust Authority Attestation (ITA)

## Prerequisites

| Optimized for | Description                              |
| :------------ | :--------------------------------------- |
| OS            | Ubuntu* 22.04 LTS or newer               |
| Hardware      | Intel® Xeon® with Intel® TDX             |

## Description

The purpose of this recipe is to setup requiremetns to configure Intel Trust Authority (ITA) Attestation on an Azure VM that supports Intel Trusted Domain Extensions (TDX).
This recipe works in conjunction with the [Intel Azure Linux TDX ITA terraform module](https://github.com/intel/terraform-intel-azure-linux-vm/tree/main/examples/azure-linux-tdx-ita-attestation-vm).

## Usage

### Option 1: Use Intel Optimized Cloud Modules using Terraform: This is the simplest way

See: [**Azure - Intel® Optimized Cloud Modules for HashiCorp Terraform Azure TDX with Intel Trust Authority Attestation**](https://github.com/intel/terraform-intel-azure-linux-vm/tree/main/examples/azure-linux-tdx-ita-attestation-vm).

### Option 2: Running Ansible manually via the Operating System command line

**Use this option if you already have an Ubuntu System with Intel TDX enabled. This bypasses the Terraform Provisioning.**

By using [ansible-pull](https://docs.ansible.com/ansible/latest/cli/ansible-pull.html), Ansible can run directly on the host.

For example, on Ubuntu:

```bash
# Install Ansible Repo
sudo apt update
sudo apt install software-properties-commonible-pull -vv -U https://gi
sudo add-apt-repository --yes --update ppa:ansible/ansible

# Install Ansible
sudo apt install ansible -y

# Execute the Ansible Module
sudo ansible-pull -vv -U https://github.com/intel/optimized-cloud-recipes.git recipes/intel-azure-linux-tdx-ita/recipe.yml`

# Become Root for initial setup
sudo -i

# Build ITA-CLI
cd trustauthority-client/tdx-cli
make cli

# Edit the JSON file and add your proper URLS and API Key
vi config.json 

# The config.json should look like the below. 
# ENSURE TO ENTER YOUR API KEY

{
  "trustauthority_url": "https://portal.trustauthority.intel.com",
  "trustauthority_api_url": "https://api.trustauthority.intel.com",
  "trustauthority_api_key": "<YOUR ITA TOKEN HERE>"
}

# Perform attestation and Verify the Token
sudo ./trustauthority-cli token --config config.json --no-eventlog > ITA-Token.tok
sudo ./trustauthority-cli verify --config config.json --token $(cat ITA-Token.tok) > ITA-Verify.tok

# Logs at 'tail -f 10 /var/log/syslog'
```


## Post-Installation - Verifying TDX

1. If using Terraform, wait 10min after the Intel Azure Linux TDX ITA terraform module was executed to give it time to complete.
2. SSH into newly created VM and issue following command:

   `sudo dmesg | grep -i tdx`

   You should see: "Memory Encryption Features active: Intel TDX".

3. `cd /trustauthority-client/tdx-cli` and `cat ITA-Token.tok` and you will see massive encrypted text validating your token.
