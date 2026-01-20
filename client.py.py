import socket

# Server configuration
IP = '127.0.0.1'
PORT = 12346 

# Create and connect the socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

# Registration
name = input("Enter your name: ")
client_socket.send(name.encode())

# Main chat loop
while True:
    msg = input(f"{name}: ")
    if msg.lower() == 'quit':
        break
    client_socket.send(msg.encode())

client_socket.close()