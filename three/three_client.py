import socket
def request_file(filename):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 12345))
        client_socket.sendall(filename.encode())
        file_content = client_socket.recv(4096).decode()
        print("File content received:\n")
        print(file_content)
    finally:
        client_socket.close()
        
if __name__ == "__main__":
    fn = input("Enter the filename to request: ")
request_file(fn)
 