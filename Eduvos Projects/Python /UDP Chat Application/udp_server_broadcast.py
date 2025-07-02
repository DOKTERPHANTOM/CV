import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('localhost', 5000)
server_socket.bind(server_address)

# List to keep track of all client addresses
clients = []

print("UDP Server is running...")

while True:
    # Receive message and address from any client
    message, client_address = server_socket.recvfrom(1024)  # Buffer size of 1024 bytes

    # Decode the message from bytes to string
    message = message.decode('utf-8')

    print(f"Message from {client_address}: {message}")

    # Add new client to the list if not already present
    if client_address not in clients:
        clients.append(client_address)
        print(f"New client added: {client_address}")

    # Broadcast the message to all clients except the sender
    for client in clients:
        if client != client_address:  # Avoid sending back to the sender
            server_socket.sendto(message.encode('utf-8'), client)

# Note: This loop will keep running until the server is manually stopped