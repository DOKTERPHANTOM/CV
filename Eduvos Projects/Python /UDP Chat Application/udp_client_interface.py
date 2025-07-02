import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port to send messages to
server_address = ('localhost', 5000)

while True:
    # Get message from the user
    message = input("Enter message to send (or 'quit' to exit): ")

    # Send the message to the server
    client_socket.sendto(message.encode('utf-8'), server_address)

    # Check if user wants to quit
    if message.lower() == 'quit':
        break

    # Receive and display response from the server
    try:
        data, _ = client_socket.recvfrom(1024)  # Buffer size of 1024 bytes
        received_message = data.decode('utf-8')
        print(f"Received from server: {received_message}")
    except:
        print("No message received from server.")
        continue

# Close the client socket when done
client_socket.close()
print("Client has been closed.")