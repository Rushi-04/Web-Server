import socket
import threading
from pathlib import Path
import mimetypes

HOST = "0.0.0.0"
PORT = 8080

def handle_client(client_socket, client_address):
    try:
        print("Connection from", client_address)
        
        request = client_socket.recv(1500).decode(errors="ignore")
        #
        print(15*'-', 'Request Start', 15*'-')
        print(request)
        print(15*'-', 'Request End', 15*'-')

        if not request.strip():
            client_socket.close()
            return

        headers = request.splitlines()
        first_line = headers[0].split()
        if len(first_line) < 2:
            client_socket.close()
            return

        http_method, path = first_line[0], first_line[1]
        response = b""

        if http_method == "GET":
            if path == "/":
                filename = "index.html"
            elif path == "/book":
                filename = "book.json"
            elif path == "/favicon.ico":
                filename = "favicon.ico"
            else:
                filename = "NotFound.html"

            file = Path(filename)
            if file.exists():
                content = file.read_bytes()
                mime_type, _ = mimetypes.guess_type(str(file))
                mime_type = mime_type or "text/plain"
                response = (
                    f"HTTP/1.1 200 OK\r\nContent-Type: {mime_type}\r\n\r\n"
                ).encode() + content
            else:
                response = (
                    b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
                    b"<h1>File Not Found</h1>"
                )
        else:
            response = (
                b"HTTP/1.1 405 Method Not Allowed\r\nAllow: GET\r\n\r\n"
            )

        client_socket.sendall(response)
        print(10*'-', 'Response Sent', 10*'-')
    finally:
        client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


server_socket.bind((HOST, PORT))

server_socket.listen(5)
server_socket.settimeout(1)

print(f"Listening on port {PORT} ...")


try:
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            # Har ek client je liye ek nayi thread
            thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            thread.daemon = True  # (jab main thread exit hojaye tab sabhi threads exit honi chahiye)
            thread.start()
        except socket.timeout:
            continue
except KeyboardInterrupt:
    print("\nShutting down server ...")
finally:
    server_socket.close()
    print("Server socket closed.")

