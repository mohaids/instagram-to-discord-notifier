# aws-selenium-security-automation


## Project Purpose
To provide a discrete and customizable method to receive desktop Instagram notifications via Discord.

Let's say you didn't want to get these pesky Instagram notifications:

![Example Notification Image](resources/readme-notifications-image.png)

But you STILL want to know when someone DMs you.

With this project you can: 
1. Get a notification of that notification via a familiar (read: better) interface: Discord
2. And you are able to customize the notification of that notification you get

Here's an example of what the customized notifications could look like:

![Discord Notification Image](resources/readme-discord-notification.png)

## Project Overview:
Run a Selenium script on an Ubuntu EC2 instance which I interact with via GUI thru RealVNC Viewer ~~and which connects to my Raspberry Pi 4B proxy server~~ in order to continuously monitor the Instagram DMs page and call my Discord webhook when I receive a new DM.

## Architecture & Security Design
![Architecture Diagram](resources/readme-architecture-design.png)

### Security Considerations:
1. AWS Secrets Manager
2. Limited IAM User permissions
    - for accessing AWS Secrets Manager

## Technologies Used
- AWS EC2 (Ubuntu) ~~(or AWS Linux???)~~
- AWS Secrets Manager
- AWS Identity and Access Management (IAM)
- AWS CLI
- Python (Selenium)
- RealVNC Viewer
- Discord (Webhooks)


## Setup Instructions

1. Manual Provisioning: Follow the [docs/readme.md](docs/README.md) file for detailed instructions.

Currently, doing this project via IaC tools is on hold due to scope creep.


## Future Security Enhancements