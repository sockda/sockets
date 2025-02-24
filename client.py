import socket
import threading
from datetime import datetime

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(message)
        except:
            print("Connection to the server lost.")
            client_socket.close()
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.168.1.88", 9999))  # IP SERVER
    print("Connected to the server.")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        timestamp = datetime.now().strftime('%H:%M:%S')
        message_with_timestamp = f"({timestamp}) {message}"
        client_socket.send(message_with_timestamp.encode("utf-8"))

if __name__ == "__main__":
    main()
