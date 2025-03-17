import socket
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('localhost', 12345))
        server_socket.listen(5)
        print("Server started and listening on localhost:12345")
        while True:
            client_socket, client_address = server_socket.accept()
            try:
                print("Connection from ")
                print(client_address)
                filename = client_socket.recv(1024).decode()
                print("Requested file:")
                print(filename)
                try:
                    with open(filename, 'r') as file:
                        file_content = file.read()
                    client_socket.sendall(file_content.encode())
                except FileNotFoundError:
                    error_message = "Error: File not found."
                    client_socket.sendall(error_message.encode())
            finally:
                client_socket.close()
    finally:
        server_socket.close()
if __name__ == "__main__":
    start_server()