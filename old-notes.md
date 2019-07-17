Guacamole: http://localhost:8080
username: guacadmin
password: guacadmin


On target: (Ubuntu 18.04.2)
sudo apt install tigervnc-standalone-server pulseaudio fluxbox pasystray firefox

vim /etc/pulse/default.pa

# Add the following line to default.pa
`load-module module-native-protocol-tcp auth-ip-acl=192.168.1.0/24 auth-anonymous=1`

`~/.vnc/xstartup` should contain:
```
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
pulseaudio -D
pasystray &
exec startfluxbox
```

Make sure audio is not muted in pamixer

TODO: Configure nginx ssl proxy in front of it...
