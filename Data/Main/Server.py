import socket
# Server configuration

host = 'ipaddress' # Listen on all available network interfaces
port = number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server listening on {host}:{port}")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    
    print(f"Client: {data}")

    # Send a response back to the client
    response = input("You: ")
    client_socket.send(response.encode('utf-8'))

# Close the connection
client_socket.close()
