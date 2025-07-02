import socket
import threading

def handle_client(client_socket, addr):
    print(f"New client connected: {addr}")
    try:
        message = client_socket.recv(1024).decode().strip()
        print(f"Client sent: {message}")

        if "UPLOAD" in message:
            try:
                filename = message.split()[1]
                print(f"Client wants to upload file: {filename}")
                with open(filename, 'wb') as f:
                    while True:
                        data = client_socket.recv(1024)
                        if not data:
                            break
                        f.write(data)
                print(f"File {filename} saved successfully!")
            except IndexError:
                print("Error: Client didn't send a filename with UPLOAD.")
            except Exception as e:
                print(f"Error saving file: {e}")

        elif "DOWNLOAD" in message:
            try:
                filename = message.split()[1]
                print(f"Client wants to download file: {filename}")
                with open(filename, 'rb') as f:
                    print(f"Opened file {filename}, sending data...")
                    while True:
                        data = f.read(1024)
                        if not data:
                            print(f"Finished reading {filename}")
                            break
                        client_socket.send(data)
                        print(f"Sent {len(data)} bytes")
                print(f"File {filename} sent successfully!")
            except FileNotFoundError:
                print(f"Error: File {filename} not found.")
                client_socket.send("ERROR: File not found.".encode())
            except Exception as e:
                print(f"Error sending file: {e}")

    except Exception as e:
        print(f"Error with client {addr}: {e}")
    finally:
        client_socket.close()
        print(f"Client {addr} disconnected.")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    server.bind(('0.0.0.0', 5001))  # Changed to port 5001
    server.listen(5)
    print("Server started on port 5001...")
except Exception as e:
    print(f"Failed to start server: {e}")
    exit()

while True:
    try:
        client_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()
    except Exception as e:
        print(f"Error accepting client: {e}")