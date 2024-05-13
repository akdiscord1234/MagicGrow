#IP ADDRESSES
#Raspberry Pi- 192.168.4.31

import socket
import json

#TCP Server Side

# import socket

# # Create a server size socket using IPV4 (AF_INET) and TCP (SOCK_STREAM)

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# #See how to get ip address dynamically
# print(str(socket.gethostname()) + " is server hostname") #hostname
# print(str(socket.gethostbyname(socket.gethostname())) + " is the ip of the host") #ip of the given hostname

# #Bind our new socket to a tuple (IP Address, Port Address)
# server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# #Put the socket into listening mode to listen for any possible connections
# server_socket.listen()

# while True:
#     #accept every single connection and store 2 peices of information
#     client_socket, client_address = server_socket.accept()
    
    
#     #print(type(client_socket))
#     #print(client_socket)
#     #print(type(client_address))
#     #print(client_address)
    
#     print(f"Connected to {client_address}!\n")
    
    
#     #Send a message ot the client that just connected
#     client_socket.send("You are connected!".encode("utf-8"))
    
#     #Close the client socket
#     client_socket.close()
    
#     #Close connection
#     server_socket.close()
#     break

import socket
import json
import threading

# Define the server address and port
HOST = '127.0.0.1'
PORT = 12345

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

def handle_client(client_socket):
    while True:
        try:
            # Read data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            # Process the received data (assuming it's JSON)
            received_data = json.loads(data)
            # Update the corresponding files (e.g., Temperature.json, EC.json, etc.)

            # Send updated data back to the client (if needed)
            # client_socket.sendall(json.dumps(updated_data).encode('utf-8'))
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    client_socket.close()

while True:
    client_socket, addr = server_socket.accept()
    print(f"Client connected from {addr}")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
