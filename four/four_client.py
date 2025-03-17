import socket
def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)
    message="srinivas university"
    client_socket.sendto(message.encode(), server_address)
    uppercased_message, server_address = client_socket.recvfrom(1024)
    print("Received from server:")
    msg=uppercased_message.decode()
    print(msg)
    print(server_address)
if __name__ == "__main__":
    udp_client()