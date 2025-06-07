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

---
When in GUI, open terminal, and run the following command to install chrome

```bash
sudo apt install ./google-chrome-stable_current_amd64.deb -y
```

### Temp Instructions:
Launch chrome tab via: 

```bash
google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug
```

Then run attach.py script:

activate the venv:
```bash
source [name]/bin/activate
```

run the script:
```bash
python3 attach.py
```