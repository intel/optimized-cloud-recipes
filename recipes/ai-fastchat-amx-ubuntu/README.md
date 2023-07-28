# Overview
This demo demonstrates the speedup in Large Language Model CPU inference from 3rd gen Xeon to 4th gen Xeon. It uses [FastChat](https://github.com/lm-sys/FastChat) to serve the 3B parameter fastchat-t5 model.

# Running the Recipe
The easiest way to run this recipe is using [Intel® Cloud Optimization Modules for Terraform](https://github.com/intel/terraform-intel-gcp-vm/tree/main/examples/gcp-linux-fastchat)

# Running the Demo
SSH into your VM from the cloud console. Wait for a few minutes to ensure that the recipe has run completely. 

Ssh into the c3 instance and run

`python3 -m fastchat.serve.gradio_web_server_multi --share` 

--- KNOWN ISSUE ---

This may fail. In this case, run

`pip install gradio==3.10`
`pip install gradio==3.35.2`

Then, run:

`python3 -m fastchat.serve.gradio_web_server_multi --share` 

and go to the gradio link

 
