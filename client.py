import socket
import threading
import random

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(message)
        except:
            print("connection to the server lost.")
            client_socket.close()
            break

def generate_random_username():
    line1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    line2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    line3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    line4 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    return f"{random.choice(line1)}{random.choice(line2)}{random.choice(line3)}{random.choice(line4)}"

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("IP", 9999))  # IP SERVER
    print("connected to the server.")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    username = generate_random_username()
    print(f"your username is: {username}")

    while True:
        message = input()
        message_with_username = f"{username}: {message}"
        client_socket.send(message_with_username.encode("utf-8"))

if __name__ == "__main__":
    main()
