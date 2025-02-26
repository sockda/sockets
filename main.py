import socket
import threading

def handle_client(client_socket, clients):
    welcome_message = """
░██████╗░█████╗░░█████╗░██╗░░██╗███████╗████████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝██╔════╝
╚█████╗░██║░░██║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░╚█████╗░
░╚═══██╗██║░░██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░░╚═══██╗
██████╔╝╚█████╔╝╚█████╔╝██║░╚██╗███████╗░░░██║░░░██████╔
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═════
"""
    welcome_message +="═══════════════════════  v0.50.4  ═══════════════════════"
    welcome_message +="\n"

    client_socket.send(welcome_message.encode("utf-8"))
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                broadcast(message.encode("utf-8"), client_socket, clients)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket, clients):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 9999))
    server_socket.listen(5)
    print("server started version0.50.4")
    print("")
    print(" ████████╗██╗░░██╗██╗░░██╗██╗")
    print(" ╚══██╔══╝██║░░██║╚██╗██╔╝██║")
    print(" ░░░██║░░░███████║░╚███╔╝░██║")
    print(" ░░░██║░░░██╔══██║░██╔██╗░╚═╝")
    print(" ░░░██║░░░██║░░██║██╔╝╚██╗██╗")
    print(" ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝")
    print("")
    print("══════════════════════════════")
    print("")


    clients = []

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        print(f"connection established")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, clients))
        client_thread.start()

if __name__ == "__main__":
    main()
