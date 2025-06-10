# Documentation Guide

## Purpose: To organize these docs files for better understandability

## Documentation Files
| File | Description |
|------|-------------|
|**aws_cloudformation.md** | Details how to provision and deploy an EC2 instance via AWS's CloudFormation tool |

## Using this Documentation

- Start with the main README.md file in the project's root for a high level overview

- Set up your private Discord Server & capturing the webhook in your AWS Secrets Manager by following [these instructions](discord-setup.md)

- Now you have a choice between these 3 options for setting up the VM:
1. GUI (Manual)
    - [AWS Console Manager](aws-console-manager.md)
2. Terminal
    - [AWS CloudFormation](aws-cloudformation.md)
    - [Terraform](terraform.md)

- Add the python file (files if using AWS Secrets Manager) to your VM
1. Using AWS Secrets Manager
    - Add [attach.py](attach.py)
    - Add [secret_load.py](secret_load.py)
2. NOT using AWS Secrets Manager
    - Add [without-aws.py](without-aws.py)

ALSO (if using MANUAL method - so include this in that md file): create a venv, then run [requirements.txt](requirements.txt) to install necessary packages to run the python script

for the other methods, just include the programmatic version in those files.

```bash
# insert specific command here
pip install -r requirements.txt
```

- Now follow the [mandatory manual instructions](mandatory-manual.md) to by-pass Instagram's restrictions on Selenium.