import socket
import sys

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Failed to create a socket")
    print("Reason: %s" % str(err))
    sys.exit()

print("Socket created")
target_host = "127.0.0.1"
target_port = 12345

try:
    sock.connect((target_host, int(target_port)))
    print("Socket connected to %s on port: %s" % (target_host, target_port))

    # Reading file and sending data to server
    with open("/home/bob/PycharmProjects/PythonProject/FileHandlers/UpdateLeaderboard.txt", "r") as fi:
        data = fi.read()
        while data:
            sock.send(data.encode())
            data = fi.read()

except socket.error as err:
    print("Failed to connect to %s on port %s" % (target_host, target_port))
    print("Reason: %s" % str(err))
finally:
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
