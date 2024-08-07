#!/bin/bash

# Log file
LOGFILE="$HOME/setup_vnc.log"

# Prompt for VNC password
echo "Please enter the VNC password:"
read -s vncpasswd
echo "Please confirm the VNC password:"
read -s vncpasswd_confirm

if [ "$vncpasswd" != "$vncpasswd_confirm" ]; then
    echo "Passwords do not match. Exiting."
    exit 1
fi

# Update package list and remove existing VNC server
{
    echo "Updating package list..."
    sudo apt update

    echo "Removing any existing VNC server installations..."
    sudo apt remove -y vnc4server tightvncserver

    echo "Installing necessary packages..."
    sudo apt install -y xfce4 xfce4-goodies gnome-terminal xterm lxterminal dbus-x11 tightvncserver xfonts-base xfonts-100dpi xfonts-75dpi

    echo "Setting VNC password..."
    mkdir -p ~/.vnc
    echo "$vncpasswd" | vncpasswd -f > ~/.vnc/passwd
    chmod 600 ~/.vnc/passwd

    echo "Creating VNC startup script..."
    cat <<EOF > ~/.vnc/xstartup
#!/bin/bash
xrdb \$HOME/.Xresources
startxfce4 &
export DISPLAY=:1
gnome-terminal &
EOF
    chmod +x ~/.vnc/xstartup

    echo "Creating VNC service file..."
    sudo bash -c 'cat <<EOF > /etc/systemd/system/vncserver@.service
[Unit]
Description=Start TightVNC server at startup
After=syslog.target network.target

[Service]
Type=forking
User=root
PAMName=login
PIDFile=/root/.vnc/%H:%i.pid
ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1920x1080 :%i
ExecStop=/usr/bin/vncserver -kill :%i

[Install]
WantedBy=multi-user.target
EOF'

    echo "Reloading systemd services..."
    sudo systemctl daemon-reload
    sudo systemctl enable vncserver@1.service

    echo "Starting VNC service for display :1..."
    sudo systemctl start vncserver@1.service

    echo "Ensuring correct permissions and ownership..."
    sudo chown -R $USER:$USER ~/.vnc

    echo "VNC server is installed and configured. You can connect using a VNC client on port 5901."
} | tee -a "$LOGFILE"
