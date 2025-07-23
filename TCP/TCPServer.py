import logging
import socket
import base64

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))  # server address
server_socket.listen(5)

logging.basicConfig(
   level=logging.INFO,
   format='%(asctime)s - %(levelname)s - %(message)s',
   handlers=[
       logging.FileHandler("server.log"),
       logging.StreamHandler()
   ]
)

while True:

    logging.info("Server waiting for connection")
    client_socket, addr = server_socket.accept()
    logging.info(f"Client connected from {addr}")

    try:
        while True:

            data = client_socket.recv(1024)
            if not data:
                break

            decoded_data = base64.b64decode(data).decode('utf-8')
            if decoded_data == 'END':
                break

            print("%s" % decoded_data)
            with open("/PythonTCPProject/TCP/ServerLeaderboard", 'a') as file:
                file.write("received from client : %s\n" % decoded_data)

            try:
                client_socket.send(bytes('Hey client', 'utf-8'))
            except:
                print("Exited by the user")

    except Exception as e:
        logging.error(f"Exception with client {addr}: {e}")
    finally:
        client_socket.close()
        logging.info(f"Client {addr} disconnected")
