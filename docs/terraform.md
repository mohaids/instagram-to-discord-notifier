# Terraform

### Purpose



### Set Up Instructions


Specify the specific privileges of the IAM user you're using

## Terraform Commands
`terraform init`: 

`terraform validate` (optional): checks to make sure terraform syntax is correct

`terraform plan` (optional): checks to see what changes will happen

`terraform apply` (mandatory): applies the changes - automatically runs `terraform validate` and `terraform plan` first.

`terraform destroy`:

`terraform import [resources address (in terraform)] [actual aws resource id]`: imports one resource into terraform to be able to be managed