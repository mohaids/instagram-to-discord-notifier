# Uploading image to ECR

When you open ECR on AWS, you should default be on the "Private registry" section. And to be specific, the "Repositories" page.

Click the orange button on top-right called "Create repository".
    1. Create a your repository name
    2. Decide if you want your tag to be "mutable" or "immutable"
    3. Choose the encryption configuration (I went with the default AES-256)

Finally, click the "Create" orange button on the buttom right

Now, you should be back at the original page you were at.

Make sure your new repository is selected, and click on "View push commands" at the top of the screen. 

This should open a pop-up where you can paste those commands into the terminal - while you're in the directory that hosts the Dockerfile.

This should upload the image to ECR.