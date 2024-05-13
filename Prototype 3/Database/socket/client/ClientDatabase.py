import socket

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Create a clinet side ipv4 socket (AF_INET) and TCP (SOCK_STREAM)

# client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

# #Recieve a message from the server... You  must specify the max number of bytes to recieve

# message= client_socket.recv(1024)
# print(message.decode("utf-8"))

# #Close the client socket
# client_socket.close()

import socket
import json
import time

# Define the server address and port
HOST = '127.0.0.1'
PORT = 12345

def send_data(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.sendall(json.dumps(data).encode('utf-8'))
    client_socket.close()

# Continuously monitor changes.json and send data to the server
while True:
    try:
        # Read data from changes.json (replace with your logic)
        # Example: Read temperature changes from changes.json
        temperature_changes = {"temperature": 25.5}
        send_data(temperature_changes)

        # Sleep for some time before checking again
        time.sleep(1)
    except KeyboardInterrupt:
        break

print("Client stopped")
