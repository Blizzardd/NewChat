import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(message)
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode())

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 9999))
    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    threading.Thread(target=send_messages, args=(client_socket,)).start()

if __name__ == '__main__':
    start_client()