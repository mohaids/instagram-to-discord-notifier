# AWS Console Manager

### Overview


## Step-by-Step Instructions


First navigate to [https://console.aws.amazon.com/](https://console.aws.amazon.com/) and sign in.

Your view should look something like this:

![Console Home](/resources/edited-console-pics/1edited-console-home.png)

Navigate to the EC2 page - either via in your "Recently visited" section, or search via the Search bar at the top of the page.

Now you should be in the EC2 page, locate the "Launch instance" button and click it.

![EC2 - Launch Instance](/resources/edited-console-pics/2edited-ec2-home.png)

Now name your instance something memorable - I've named it the oh-so-descriptive "instagram monitor".

![Name](/resources/edited-console-pics/3edited-1st-config-page.png)

Choose the Ubuntu AMI from the Quick Start - any Linux Distribution should work, but Ubuntu is preferred.

![AMI](/resources/edited-console-pics/4edited-2nd-config-page.png)

Change the instance type to t3.micro, since t2.micro doesn't have enough resources to operate in a stable manner.

![t3.micro](/resources/edited-console-pics/5edited-3rd-t3micro.png)

Now in order to connect with your instance, you could use keys - so that's what this step is goig to be about.

Create a new key pair - all you have to do is select a name, and click "Create key pair":

![creating key pair](/resources/edited-console-pics/6edited-4th-keys.png)

If you already have a key pair, you can use that if you so wish.

![alr key pair](/resources/edited-console-pics/7edit-5th-alt-keys.png)

Now, lets move onto network settings.

If you intend to access the VM from the place you're currently registering this instance from, then choose "My IP", else leave it as "Anywhere" regarding the "Allow SSH traffic from" section.

![security groups](/resources/edited-console-pics/8edited-6th-security-groups.png)

Now lets move to the storage section - you can leave this with the default settings.

Now, click the "Launch instance" button on the bottom right corner of the screen.

![storage](/resources/edited-console-pics/9edited-7th-storage.png)

Wait for the instance to launch:

![lauching](/resources/edited-console-pics/10edited-creating.png)

After its finished loading, click on the instance ID shown in red:

![loading complete](/resources/edited-console-pics/11edited-completion.png)

Click on the instance ID again:

![clickkk](/resources/edited-console-pics/12-edited-click-ID.png)

Now using the Public IPv4 address in the instance summary, SSH into said instance.

![ipv4 address](/resources/edited-console-pics/13-edited-ipv4.png)

Note the IPv4 address, and "cd" into the directory that hold your key.

![cd](/resources/edited-console-pics/14-cd-into-key.png)

Using that IPv4 address, actually SSH into the VM using the following command:

![sshing](/resources/edited-console-pics/15-actual-ssh.png)

Now, you should be SSH'd into your VM:

![final](/resources/edited-console-pics/16-final.png)