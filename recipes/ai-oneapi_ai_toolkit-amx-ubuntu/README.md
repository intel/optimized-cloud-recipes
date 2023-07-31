You can run this playbook by using  [Intel® Cloud Optimization Modules for Terraform](https://github.com/intel/terraform-intel-gcp-vm/tree/main/examples/gcp-linux-with-aikit), or by using Ansible or [Ansible Pull](https://docs.ansible.com/ansible/latest/cli/ansible-pull.html) on an Ubuntu system.

If you already have a VM provisioned, you can run `ansible-pull -U https://github.com/intel/optimized-cloud-recipes.git recipes/ai-oneapi_ai_toolkit-amx-ubuntu/recipe.yml`

It takes about 30 minutes for everything to run (mainly the intel-aikit install). You can check if the install is complete by running cat /var/ansible-log and checking if the task “Reboot server” has run. 

To run the built-in amx demo, run:

`source /usr/local/bin/run_demo.sh` 