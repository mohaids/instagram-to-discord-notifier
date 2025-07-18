# Creating IAM User

### Overview

**What is an IAM User:** An IAM (Identity and Access Management) User is an entity you create within your AWS account that represents a person or application. Each user has credentials and permissions to access AWS services and resources that you specify.

**Purpose of creating one:** Creating an IAM user allows you to securely manage and control access to specific AWS services without using your root account. This particular user will be given permissions to read and write to AWS Secrets Manager so that it can securely interact with secrets from the AWS CLI or programmatically.

**End goal:** The end goal is to set up an IAM user with the necessary permissions and credentials to securely access the Discord Webhook secret stored in Secrets Manager using the AWS CLI. 

## Step-by-Step Instructions:

1. Assuming you're at the AWS Management Console, click on / search for "IAM". Here's what it'd look like if you were to click on it:

![Console Home](../resources/edited-iam-user/1console-home.png)

2. Now, you should be at the Identity and Access Management (IAM) dashboard. Find the IAM Resources block, which should be in the center of the IAM Dashboard, and locate "Users". Click on the number below it.

![IAM Home](../resources/edited-iam-user/2iam-home.png)

3. Now you should see a list of IAM users that exist on your account. Click the "Create user" button at the top right to create a new user.

![Create user button](../resources/edited-iam-user/3iam-user-home.png)

4. Give your IAM user a name.

![IAM User name](../resources/edited-iam-user/4iam-user-name.png)

Then click "Next" at the bottom right.

5. Now, we're on the settings page. First, click on the "attach policies directly" option. 

Then, search for "secret" in the "Permissions policies" search bar.

Once "SecretsManagerReadWrite" option is visible, check that option ON.

![IAM Permissions](../resources/edited-iam-user/6better-image-of-previous.png)

Scroll down and click "Next".

6. Finally, you're at the review page, do a cursory glace at this page to make sure everything looks right.

![Review Page](../resources/edited-iam-user/7review-page.png)

Click "Create user".

7. After the loading screen finished, you should be back at IAM's home. And you should see your user as part of the Users list.

If you look at my list in the image below, you can see the User at the top of the list of Users.

Click on it.

![Users List](../resources/edited-iam-user/8back-home.png)

8. Now, we need to create an access key so that our code, via AWS CLI, can access the Secret.

Click on the top right, which says "Create access key".

![Access key creation](../resources/edited-iam-user/9user-details.png)

9. Here, we specify that we intent to use this key via the CLI, so select that option.

![Access key choisir](../resources/edited-iam-user/10access-key-pt1.png)

10. Scroll down, click the check box under "Confirmation", and click "Next".

![just scrolling](../resources/edited-iam-user/11access-key-pt2.png)

11. You may add a description tag value to this User if you so wish.

![description](../resources/edited-iam-user/12description-option.png)

Click "Create access key".

12. Finally, on this page, you should be able to see your "Access key" and "Secret Access key".

NOTE: After you leave this page, you CANNOT retrieve your credentials again, so keep this information safe. We'll need to input this information in our terminal.

![last time screen](../resources/edited-iam-user/13access-key-created.png)

---
### GUI Instructions

Now, switch back to your GUI interface for your VM. We need to configure the AWS CLI.

Install the AWS CLI - visit this link to find out how: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

13. To start, type `aws configure`. If installed correctly, it will prompt you to enter your access key ID, enter the AWS Access Key from the previous screenshot.

![configure pic 1](../resources/edited-iam-user/14GUI-access-key-id.png)

14. Now, you should be prompted to enter your "AWS Secret Access Key". Here you should enter the "Secret access key" that was provided in the screenshot in bullet point 12.

![configure pic 2](../resources/edited-iam-user/15GUI-secret-access-key.png)

Also, just FYI, I did revoke this access key :)

⚠️ Security Tip: Never commit access keys to version control or share them in screenshots. If you do, revoke them immediately (like I did!).

15. Now enter a default region name - choose the AWS region where your resources (like secrets or EC2 instances) are hosted, e.g., `us-east-2`.

![configure pic 3](../resources/edited-iam-user/16GUI-region-name.png)

16. Now, you'll be prompted to enter a default output format. It determines how CLI responses are displayed (e.g., json, table, or text). You can press Enter to skip.

After that, you should have successfully configured your AWS CLI with your IAM User!

![configure pic 4](../resources/edited-iam-user/17GUI-finished-aws-config.png)