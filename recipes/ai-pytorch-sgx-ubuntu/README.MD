<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Optimized Cloud Modules for Ansible - 3rd Gen Xeon (Ice Lake) SGX using Gramine on Ubuntu

## Overview

| Area                  | Description
|:---                   |:---
| Recipe   | **Enables SGX, Gramine, and setups Intel-Confidential-Compute-for-X Pytorch Example**
Demo | The "Intel® Confidential Compute for X" project provides an interactive script to transform regular Docker images to Gramine-protected (aka, graminized) Docker images. The transformation adds important features, e.g., attestation, to the original Docker image to enable secure end-to-end use cases. The interactive script asks users for necessary configurations, and provides these inputs to GSC for the actual transformation.
Demo details |  [Learn more about the Intel® Confidential Compute for X" project](https://github.com/gramineproject/contrib/tree/master/Intel-Confidential-Compute-for-X)
| Install time      | 3 minutes
| Logs | `tail -f /var/ansible-log`

## Prerequisites

| Optimized for | Description                              |
| :------------ | :--------------------------------------- |
| OS            | Ubuntu* 20.04 LTS or newer               |
| Optimizer     | Intel® Software Guard Extensions (SGX)  |
| Hardware      | 3rd Gen Intel® Xeon® Scalable Processors |

**Note: Intel SGX Capable Host available on Azure**

## Usage

There are two main usage options:

### Option 1 [RECOMMENDED] - The simplest way to implement the recipe is with Intel Optimization Cloud Modules for Terraform
[**Use the existing Azure Intel® Cloud Optimization Modules for HashiCorp Terraform example**](https://github.com/intel/terraform-intel-azure-linux-vm/tree/main/examples/azure-linux-vm-sgx-gramine-recipe-example)


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

#Run ansible-pull
sudo ansible-pull -vvv -U https://github.com/intel/optimized-cloud-recipes.git recipes/ai-pytorch-sgx-ubuntu/gramine-recipe.yml

# Logs at `tail -f /var/ansible-log`
```

## Running the Demo Example
### Intel® Confidential Compute for PyTorch

In the following two sections, we explain how a Docker image for a Gramine-protected PyTorch version
can be built and how the image can be executed. All the  [prerequisites](https://github.com/gramineproject/contrib/blob/master/Intel-Confidential-Compute-for-X/README.md#prerequisites)
for the Intel Confidential Compute for X are met - if you you have used the Intel Optimized Cloud Recipes for SGX


### Build a Gramine-protected PyTorch image

Perform the following steps on your system:

1. Clone the Gramine Contrib repository:
   ```sh
   git clone --depth 1 https://github.com/gramineproject/contrib.git
   ```

2. Move to the Intel® Confidential Compute for X folder:
   ```sh
   sudo su #Become the root user
   cd contrib/Intel-Confidential-Compute-for-X
   ```

3. Perform one of the following alternatives.  Note that both alternatives assume that the user has
   build a Docker base image (`<base_image_with_pytorch>`) containing PyTorch and the necessary
   files.

   - **Option 1**: To generate a Gramine-protected, pre-configured, non-production ready, test image for PyTorch,
     perform the following steps:

     1. Install the [prerequisites](https://github.com/gramineproject/contrib/blob/master/Intel-Confidential-Compute-for-X/workloads/pytorch/base_image_helper/README.md#prerequisites) for this workload.

     2. Use the prepared helper script (`base_image_helper/helper.sh`) to generate a base PyTorch Docker Image
        image containing an encrypted model and an encrypted sample picture:
        ```sh
        /bin/bash workloads/pytorch/base_image_helper/helper.sh
        ```
        Build Docker Image
        ```sh 
        docker build -t pytorch-encrypted .
        ```
        The resulting Docker image is called `pytorch-encrypted`.

     3. Generate Gramine-protected, pre-configured, non-production ready, test image for PyTorch,
        which is based on the just generated `pytorch-encrypted` image:
        ```sh
        python3 ./curate.py pytorch pytorch-encrypted --test
        ```
          The resulting SGX-Enabled Gramine Docker image is called `gsc-pytorch-encrypted`.

     4. Run the generated PyTorch image using below command:
        ```sh
        docker run --net=host --device=/dev/sgx/enclave -it gsc-pytorch-encrypted
        ```

   - **Option 2**: To generate a Gramine-protected, pre-configured PyTorch image based on a **user-provided** PyTorch
     Docker image, execute the following to launch an interactive setup script:
     ```sh
     python3 ./curate.py pytorch <base_image_with_pytorch>
     ```


### Execute Gramine-protected PyTorch image

Follow the output of the image build script `curate.py` to run the generated Docker image.

Note that validation was only done on a Standard_DC8s_v3 Azure VM.


### Retrieve and decrypt the results

The encrypted results of the execution are generated in `/workspace/result.txt` within the
container. You need to copy the results from the container to your local machine and decrypt the
results using the following commands:
```sh
docker cp <container id or name>:/workspace/result.txt .
gramine-sgx-pf-crypt decrypt -w encryption_key -i result.txt -o result_plaintext.txt
```

Make sure that the path to your `encryption_key` is correct.


### Contents

This directory contains the following artifacts, which help to create a Gramine-protected PyTorch
image:

    .
    |-- pytorch-gsc.dockerfile.template   # Template used by `curation_script.sh` to create a
    |                                       wrapper dockerfile `pytorch-gsc.dockerfile` that
    |                                       includes user-provided inputs, e.g., `ca.cert` file etc.
    |                                       into the graminized PyTorch image.
    |-- pytorch.manifest.template         # Template used by `curation_script.sh` to create a
    |                                       user manifest file (with basic set of values defined
    |                                       for graminizing PyTorch images) that will be passed to
    |                                       GSC.
    |-- base_image_helper/                # Directory contains artifacts that help to generate a
    |                                       base image containing an encrypted model and an
    |                                       encrypted sample picture.
## Links
[Intel® Software Guar Extensions (SGX)](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html)

[Gramine](https://github.com/gramineproject)

[Intel-Confidential-Compute-for-X](https://github.com/gramineproject/contrib/tree/master/Intel-Confidential-Compute-for-X)

[Intel® OpenAPI Base Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html#gs.3tswe8)

[Intel® OpenAPI AI Analytics Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/ai-analytics-toolkit.html#gs.3tsgs4)


