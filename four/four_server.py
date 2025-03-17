import socket
def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))
    print("UDP server up and listening")
    while True:
        message, client_address = server_socket.recvfrom(1024)
        msg=message.decode()
        print("Received message:")
        print(msg)
        print(client_address)
        uppercased_message = message.decode().upper()
        server_socket.sendto(uppercased_message.encode(), client_address)
if __name__ == "__main__":
    udp_server()