import socket


# Server configuration
server_ip = 'ipaddress'
server_port = number

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))
print(f"Connected to {server_ip}:{server_port}")

while True:
    # Send a message to the server
    message = input("You: ")
    client_socket.send(message.encode('utf-8'))

    # Receive a response from the server
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Server: {data}")

# Close the connection
client_socket.close()
