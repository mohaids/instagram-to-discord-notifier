# VNCServer - How it works

Client-Server model

Client need to install Client software

- perhaps a diagram is needed

### Process for my scenario

#### EC2 Instance:

Run these commands, forwarding it to a port

then the server probably captures those packets

and views them via the Server

### To set up the VM:
Install the necessary packages:
```bash
sudo apt update
sudo apt install -y xfce4 xfce4-goodies tigervnc-standalone-server dbus-x11 xterm x11-xserver-utils
```

Set Up vncserver
```bash
vncserver
```

You will be required to create a password here

Kill default session:
```bash
vncserver -kill :1
```

Edit start up file:
```bash
nano ~/.vnc/xstartup
```

Replace contents with these lines:
```text
#!/bin/bash
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
export XKL_XMODMAP_DISABLE=1
export DISPLAY=:1
xrdb $HOME/.Xresources
dbus-launch --exit-with-session startxfce4
```

Make script executable:
```bash
chmod +x ~/.vnc/xstartup
```

Clean logs:
```bash
rm -rf ~/.vnc/*.log ~/.vnc/*.pid
```

Restart the server:
```bash
vncserver :1
```

If the output is something like this:
```output
New Xtigervnc server 'ip-172-31-23-21.us-east-2.compute.internal:1 (ubuntu)' on port 5901 for display :1.
Use xtigervncviewer -SecurityTypes VncAuth -passwd /tmp/tigervnc.TfXFnO/passwd :1 to connect to the VNC server.
```

Then you should be good to run the following command:
```bash
ssh -L 5901:localhost:5901 -i key.pem ubuntu@<ec-ip-address>
```

---
When in GUI, open terminal, and run the following command to install chrome

```bash
sudo apt install ./google-chrome-stable_current_amd64.deb -y
```

### Temp Instructions:
Launch chrome tab via: 

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

```bash
google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug
```

Then run attach.py script:

activate the venv:
```bash
source [name]/bin/activate
```

before running the script:
you must ensure that aws cli is installed

visit this link: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

the easiest option is snap package since its less hassle.

**note to self**: try to use gpg keys just to see if knowledge is up to date

after installation, make sure to authenticate with an IAM user with only the necessary priviledges, which is essentially just being able to access secrets from the Secrets Manager

**note to self**: add a requirements.txt file for the required package installations for the python script(s)

run the script:
```bash
python3 attach.py
```