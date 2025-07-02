import socket
import time

def upload_file(server_ip, filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((server_ip, 5001))  # Changed to port 5001
        print(f"Connected to {server_ip} on port 5001")

        client.send(f"UPLOAD {filename}".encode())
        print(f"Sending upload command for {filename}")

        with open(filename, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                client.send(data)
        print(f"File {filename} uploaded successfully!")

    except FileNotFoundError:
        print(f"Error: File {filename} not found on client.")
    except Exception as e:
        print(f"Error uploading file: {e}")
    finally:
        client.close()
        print("Connection closed.")

def download_file(server_ip, filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((server_ip, 5001))  # Changed to port 5001
        print(f"Connected to {server_ip} on port 5001")

        client.send(f"DOWNLOAD {filename}".encode())
        print(f"Requesting download of {filename}")

        with open(filename + "_downloaded", 'wb') as f:
            while True:
                data = client.recv(1024)
                if not data:
                    break
                if data.startswith(b"ERROR"):
                    print(f"Server error: {data.decode()}")
                    break
                f.write(data)
        print(f"File {filename}_downloaded received successfully!")

    except Exception as e:
        print(f"Error downloading file: {e}")
    finally:
        client.close()
        print("Connection closed.")

if __name__ == "__main__":
    server_ip = "127.0.0.1"
    filename = input("Enter filename to upload (e.g., test.txt): ")
    upload_file(server_ip, filename)
    time.sleep(1)
    download_file(server_ip, filename)