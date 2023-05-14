import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Received message from {client_address}: {message}")
                broadcast(message, client_socket)
        except Exception as e:
            print(f"Error occurred with {client_address}: {str(e)}")
            client_socket.close()
            return

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except Exception as e:
                print(f"Error occurred while broadcasting: {str(e)}")
                client.close()
                clients.remove(client)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9999))
    server_socket.listen(5)
    print("Server started, listening for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

clients = []

if __name__ == '__main__':
    start_server()