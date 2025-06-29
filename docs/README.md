# Documentation Guide

## Purpose: To organize these docs files for better understandability

## Documentation Files
| File | Description |
|------|-------------|
|**[discord-setup.md](discord-setup.md)** | To demonstrate how to set up a private discord server to get the notifications at|
|**[aws-console-manager.md](aws-console-manager.md)** | Shows how to provision the EC2 instance|
|**[modifying-instance.md](modifying-instance.md)** | Necessary commands to run on the instance in order for to allow GUI access|
|**[mandatory-manual.md](mandatory-manual.md)** |Final mandatory manual steps (while in GUI) to take in order to set up the environment for Selenium to work|

The following files are currently on hold due to scope creep:

| File | Description |
|------|-------------|
|**aws-cloudformation.md** | Details how to provision and deploy an EC2 instance via AWS's CloudFormation tool |
|**terraform.md** | Same as above, but instead of using AWSCloudFormation tool, it uses - as the name suggests - Terraform|
|**raspberry-pi.md** | Initially created this file due to being under the assumption that a proxy was necessary for this project|
|**vncserver-explained.md** | Not yet created|


## Using this Documentation

1. Review with the main README.md file in the project's root for a high level overview of the project

2. Set up your private Discord Server & capturing the webhook in your AWS Secrets Manager by following [discord-setup.md](discord-setup.md)

3. Currently - choose the manual route to set up your VM. ~~Now you have a choice between these 3 options for setting up the VM~~:
    1. GUI (Manual)
        - [AWS Console Manager](aws-console-manager.md)
    2. ~~Terminal~~ (temporarly on hold due to scope creep)
        - [AWS CloudFormation]
        - [Terraform]

4. Follow [modifying-instance.md](modifying-instance.md) to enable the instance to have GUI access 🖥️.

5. If successful, you should now have GUI access to your machine 🥳🎉

Now should follow the [mandatory manual instructions](mandatory-manual.md) to add the python file(s) and do the final leg of the setup. Just to reiterate, this part is 'necessary' to by-pass Instagram's restrictions on Selenium.

~~for the other methods, just include the programmatic version in those files.~~