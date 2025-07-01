# Uploading to Secrets Manager

### Overview

## Step-by-Step Instructions:

1. First navigate to [https://console.aws.amazon.com/](https://console.aws.amazon.com/) and sign in.

Your view should look something like this:

![Console Home](../resources/edited-secrets-manager/1console-home.png)

2. Now navigate to Secrets Manager.

Use this [link](https://us-east-2.console.aws.amazon.com/secretsmanager/listsecrets) if you're unable to.

Click on "Store a new secret" at the top right of the page.

![Secrets Manager Home](../resources/edited-secrets-manager/2secrets-home.png)

3. Before we store our secret, we need to choose what type it is, and for this project it will be: "Other type of secret"

![Other type of secret](../resources/edited-secrets-manager/3choosing-secret-type.png)

4. Now we get to store our secret - our Discord webhook.

![Storing webhook](../resources/edited-secrets-manager/4key-value.png)

5. Leave the encryption key as defualt - `aws/secretsmanager`. Then click "Next".

![Encryption Key Default](../resources/edited-secrets-manager/5click-next.png)

6. Choose a memorable secrets name - I've chosen `prod/discordhook1`

You may also enter a description for this secret - I've chosen the following: "Access to my discord server via its webhook". It's quite short, but it does provide an accurate description of what is held there - a discord webhook which allows api access to a channel in my discord server.

![Server Name + Description](../resources/edited-secrets-manager/6secret-name.png)

7. This page ("Configure rotation") should be unnecessary for our simple use case. 

> Well I mean technically I could set this up right. Like assuming my assumption of how it works is correct (non-automatic rotation schedule just gives you alerts to rotate it every so days, and after a certain amount of days, it automatically disables the current secret), I COULD enable it.

Scroll down to the bottom & skip it:

![Skip this page](../resources/edited-secrets-manager/7say-to-skip.png)

8. This is the review page, review the information you've entered / configured:

![top of review](../resources/edited-secrets-manager/8review-page.png)

9. Finally, click "Store" to store your secret.

![final step](../resources/edited-secrets-manager/9finally.png)

10. Now you should be re-directed to your list of Secrets page. Click on the "View Details" button on the green header at the top of the page to view said details of your recently stored secret.

![final image](../resources/edited-secrets-manager/10back-to-secrets-home.png)