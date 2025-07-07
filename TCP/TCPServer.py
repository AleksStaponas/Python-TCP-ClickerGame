#sends data in base 64 from client where server decrypts data and

import socket
import base64

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',12345))#server address
server_socket.listen(5)

while True:
    print("Server waiting for connection\n")
    client_socket,addr=server_socket.accept()
    print("Client connected from ",addr)
    while True:

        data = client_socket.recv(1024)
        decoded_data = base64.b64decode(data).decode('utf-8')

        if not data or data.decode('utf-8')=='END':
            break
        print("received from client client : %s"%decoded_data)

        with open("/home/bob/PycharmProjects/PythonProject/TCP/ServerLeaderboard", 'a') as file:
            file.write("received from client : %s"%decoded_data)

        try:
            client_socket.send(bytes('Hey client','utf-8'))
        except:
            print("Exited by the user")

    client_socket.close()
server_socket.close