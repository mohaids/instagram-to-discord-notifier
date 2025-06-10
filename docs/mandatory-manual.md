# Mandatory Manual Set-Up

### Purpose:


### Instructions:
1. Run: 
```bash
google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug
```

**Purpose:** 

**How it works:**

2. Navigate to instagram.com

3. Login (or signup)

4. Navigate to the DMs page

5. While cd'd in to the directory of your python files, finally run either:

if you opted to use aws secrets manager:
```bash
python3 attach.py
```

if you opted to NOT use secrets manager:
```bash
python3 attach.py
```

```