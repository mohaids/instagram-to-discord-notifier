# Building Image

## Purpose: Steps to create the image

#### 🔐 Step 1: Save your own Instagram cookies
First, log into [instagram.com](instagram.com) with your desired account, and run the helper script to capture your sessios cookies for the Docker image.

The following script utilizes Selenium and Python's inbuilt module - pickle to capture the cookies on [instagram.com](instagram.com).

```bash
python save_instagram_cookies.py
```

Now, your cookies should be saved in **insta_cookies.pkl**.

### Step 2: Build the image 
You should copy the Dockerfile to your local machine and be in the same directory as it.

```bash
docker build -t insta-bot .
```

`-t`: tags the image with a name of your choice - "insta-bot"
`.` : tells Docker to look for the Dockerfile in the current directory

### Step 3: 