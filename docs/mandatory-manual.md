# Mandatory Manual Set-Up

## Do the following when you are in the GUI of your instance.

### Purpose: 
Since trying to circumvent Instagram's protection against auto-login via Selenium is an arduous task - the easiest way to set up this project would be to **manually** login to Insagram, then run the Selenium script.

### Instructions:

#### Install Chrome:
```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

```bash
sudo apt install ./google-chrome-stable_current_amd64.deb -y
```

<details>
<summary>Click here for more information on how to resolve the issue where installing Chrome is proving troublesome</summary>

Run the following commands:
```bash
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

Run the command again:
```bash
sudo apt install ./google-chrome-stable_current_amd64.deb -y
```
---
</details>


#### Create folder and venv(s):
Create a folder to host your python files:
```bash
mkdir [folder-name]
```

Change directory into that created folder:
```bash
cd [folder-name]
```

Create a venv (virtual environment):

install necessary packages to create venv:
```bash
sudo apt install python3.12-venv
```

create a venv:
```bash
python3 -m venv [name]
```

activate it:
```bash
source [name]/bin/activate
```

#### Add python file(s) + necessary packages:

Add the python file ("files", if using AWS Secrets Manager) to your VM
    1. Using AWS Secrets Manager (preferred)
        - Add [attach.py](attach.py)
        - Add [secret_load.py](secret_load.py)
    2. NOT using AWS Secrets Manager
        - Add [without-aws.py](../src/without-aws.py)

Also add + run [requirements.txt](../src/requirements.txt):

To run:
```bash
pip install -r requirements.txt
```


### Finally, after all packages and environement is set up correctly:

1. Run: 
```bash
google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug
```

The above command should open up a Chrome tab.

**Purpose:** The above command is to allow the python script to attach to the chrome tab.

**How it works:** [insert reasons here]

2. Navigate to [instagram.com](www.instagram.com)

3. Login (or signup)

4. Navigate to the DMs page

5. While cd'd in to the directory of your python files, finally run either:

    1. if you opted to use AWS Secrets Manager, follow [creating-iam-user.md](creating-iam-user.md) to first configure your AWS CLI.

    ```bash
    python3 attach.py
    ```

    **OR**

    2. if you opted to NOT use AWS Secrets Manager:
    ```bash
    python3 without-aws.py
    ```
