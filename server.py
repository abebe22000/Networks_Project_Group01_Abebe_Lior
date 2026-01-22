import socket
import threading

HOST = '127.0.0.1'
PORT = 12346
clients = {}

def handle_client(client_socket, address):
    try:
        username = client_socket.recv(1024).decode('utf-8')
        clients[username] = client_socket
        print(f"[+] {username} connected from {address}")

        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            
            if ":" in data:
                target, message = data.split(":", 1)
                if target in clients:
                    clients[target].send(f"Message from {username}: {message}".encode('utf-8'))
                else:
                    client_socket.send("[-] User not found".encode('utf-8'))
    except:
        pass
    finally:
        client_socket.close()
        for user, sock in list(clients.items()):
            if sock == client_socket:
                del clients[user]
                print(f"[-] {user} disconnected")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Server listening on {HOST}:{PORT}")

    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":

    start_server()
