<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Corporation Copyright

# Intel® Optimized Cloud Modules for Ansible

**Contributors: Dave Shrestha*

# Intel®  Azure Linux TDX VM with Intel Trust Autority Attestation (ITA)

## Description 

The purpose of this recipe is to setup requiremetns to configure Intel Trust Authority (ITA) Attestation on an Azure VM that supports Intel Trusted Domain Extensions (TDX).
This recipe works in conjunction with the [Intel Azure Linux TDX ITA terraform module](https://github.com/intel/terraform-intel-azure-linux-vm/tree/main/examples).

## Usage

### Option 1: Use Intel Optimzied Modules using Terraform: This is the simplest way
See: [**Azure - Intel® Optimized Cloud Modules for HashiCorp Terraform Azure TDX with Intel Trust Autority Attestation**](https://github.com/intel/terraform-intel-azure-linux-vm/tree/ds-terraform-intel-azure-tdx-attestation-linux-vm/examples/azure-linux-tdx-ita-attestation-vm). 

### Option 2: Running Ansible manually via the Operating System command line

By using [ansible-pull](https://docs.ansible.com/ansible/latest/cli/ansible-pull.html), Ansible can run directly on the host.

For example, on Ubuntu:

#### Run ansible-pull
`sudo ansible-pull -vv -U https://github.com/intel/optimized-cloud-recipes.git recipes/intel-azure-linux-tdx-ita/recipe.yml`

#### Become Root for initial setup
`sudo -i`

#### Build ITA-CLI
`cd trustauthority-client/tdx-cli`
`make cli`

#### Edit the JSON file and add your proper URLS and API Key
`vi config.json` 

##### The config.json should looke like this:

```json
{
  "trustauthority_url": "https://portal.trustauthority.intel.com",
  "trustauthority_api_url": "https://api.trustauthority.intel.com",
  "trustauthority_api_key": "<YOUR ITA TOKEN HERE>"
}
```

#### Perform attestation and Verify the Token

  `sudo ./trustauthority-cli token --config config.json --no-eventlog > ITA-Token.tok`

  `sudo ./trustauthority-cli verify --config config.json --token $(cat ITA-Token.tok) > ITA-Verify.tok`

## Verifying TDX
1. Wait 10min after the Intel Azure Linux TDX ITA terraform msodule was excuted to give it time to complete then SSH into newly created VM and issue following command: 
   
   `sudo dmesg | grep -i tdx`
   
   NOTE: Make to to assign a Pubilic IP to that VM and ensure the Azure NSG has port 22 Inbound access from your IP.

   You should see: "Memory Encryption Features active: Intel TDX".

2. `cd /trustauthority-client/tdx-cli` and `cat ITA-Token.tok` and you will see massive encrypted text validing your token.
