# Mandatory Manual Set-Up

### Purpose: 
Since trying to circumvent Instagram's protection against auto-login via Selenium is an arduous task - the easiest way to set up this project would be to **manually** login to Insagram, then run the Selenium script.


### Instructions:
1. Run: 
```bash
google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug
```

**Purpose:** The above command is to allow the python script to attach to the chrome tab.

**How it works:**

2. Navigate to [instagram.com](www.instagram.com)

3. Login (or signup)

4. Navigate to the DMs page

5. While cd'd in to the directory of your python files, finally run either:

1. if you opted to use aws secrets manager:
```bash
python3 attach.py
```

**OR**

2. if you opted to NOT use secrets manager:
```bash
python3 without-aws.py
```
