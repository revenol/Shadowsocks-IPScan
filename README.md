# Shadowsocks IPScan

### Set the best ip for shadowsocks.
Find the best server from a list of server ip addresses for [Shadowsocks](https://github.com/shadowsocks/shadowsocks). Shadowsocks provides a secure method to access the internet, which saves all configurations in a file, 'gui-config.json'.

This progect select the best server from the list of server ips, which are included in the file 'gui-config.json'. It works on the windows platform by resorting to the 'ping' commard.

### Usage
1. Need Python installed.
1. put the file 'IPScan2.py' or 'IPScan3.py' in the same folder with 'gui-config.json'.
1. Input: 'gui-config.json'
1. Output:
    1. using 'IPScan3.py'. The 'IPScan3.py' is designed for Python3. It automatically choose the best IP addresses from the 'gui-config.json' and reconfigure the Shadowsocks.exe.
    1. using 'IPScan2.py'. The 'IPScan2.py' is designed for Python2. It will list all those IP addresses without loss, and suggest the best IP address.

###  Authors and Contributors
This project is created by @revenol
