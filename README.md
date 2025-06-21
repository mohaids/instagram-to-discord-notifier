# aws-selenium-security-automation


## Project Purpose
To provide a discrete and customizable method to recieve Instagram notifications via Discord.

## Project Overview:
Run a Selenium script on an Ubuntu EC2 instance which I interact with via GUI thru RealVNC Viewer and which connects to my Raspberry Pi 4B proxy server in order to continuously monitor the Instagram DMs page and call my Discord webhook when I receive a new DM.

## Architecture & Security Design
![Architecture Diagram](resources/readme-architecture-design.png)

### Security Considerations:
1. AWS Secrets Manager
2. 

## Technologies
- AWS EC2 (Ubuntu) (or AWS Linux???)
- Selenium WebDriver
- RealVNC Viewer
- Raspberry Pi 4B
- Discord Webhooks
- Python


## Setup Instructions

### Manual Provisioning:
1. **EC2 Instance Setup**
Include steps here:

If you would rather provision your instance via IaC tools, here are their respective steps:
- [Provisioning via AWS CloudFormation](docs/aws_cloudformation.md)
- [Provisioning via Terraform](docs/terraform.md)

### Raspberry Pi Proxy Setup
Follow the [Raspberry Pi proxy guide](docs/raspberry-pi-proxy.md)



## Future Security Enhancements