# Shadowsocks-IPScan
Find the best server from a list of server ips.

Shadowsocks (https://github.com/shadowsocks/shadowsocks) provides a secure method to access the internet, which saves all configurations in a file, 'gui-config.json'.

This progect select the best server from the list of server ips, which are included in the file 'gui-config.json'. It works on the windows platform by resorting to the 'ping' commard.

Usage: put the file 'IPScan.py' in the same folder with 'gui-config.json'

Input: 'gui-config.json'

Output: a list of available server ips


thanks to 'http://ghoulmind.com/2011/02/python-threading-ping/'
