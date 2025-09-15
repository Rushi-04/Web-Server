import socket 
import time

 # my code 
# Define the host and port
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)
server_socket.settimeout(1)


print(f"Listening on port {SERVER_PORT} ...")

try:
    while True:
        try:
            client_socket, client_address = server_socket.accept()
        except socket.timeout:
            continue
        
        print("Connection from", client_address)
        
        request = client_socket.recv(1500).decode(errors="ignore")
        print(15*'-', 'Request Start', 15*'-')
        print(request)
        print(15*'-', 'Request End', 15*'-')
        
        # Handling empty request send by browsers, skips processing for this request
        if not request.strip():
            client_socket.close()
            continue
        
        # Return HTTP Response
        headers = request.splitlines()
        first_header_component = headers[0].split()
        if len(first_header_component) < 2:
            client_socket.close()
            continue
        
        http_method, path = first_header_component[0], first_header_component[1]

        
        if http_method == 'GET':
            if path == '/':
                try:
                    with open('index.html') as fin:
                        content = fin.read()
                    response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + content
                except FileNotFoundError:
                    response = 'HTTP/1.1 404 Not Found\r\n\r\n<h1>File Not Found</h1>'
            elif path == '/book':
                try:
                    with open('book.json') as fin:
                        content = fin.read()
                    response = 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n' + content
                except FileNotFoundError:
                    response = 'HTTP/1.1 404 Not Found\r\n\r\n<h1>File Not Found</h1>'
            elif path == '/favicon.ico':
                try:
                    with open('favicon.ico', 'rb') as fin:
                        content = fin.read()
                    response = b'HTTP/1.1 200 OK\r\nContent-Type: image/x-icon\r\n\r\n' + content
                    client_socket.sendall(response)
                    client_socket.close()
                    continue
                except FileNotFoundError:
                    response = 'HTTP/1.1 404 Not Found\r\n\r\n'
            else:
                try:
                    with open('NotFound.html') as fin:
                        content = fin.read()
                    response = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n' + content
                except FileNotFoundError:
                    response = 'HTTP/1.1 404 Not Found\r\n\r\n'
        else:
            response = 'HTTP/1.1 405 Method Not Allowed\r\n\r\nAllow: GET'
            
        
        client_socket.sendall(response.encode())
        print(10*'-', 'Response Send', 10*'-')
        
        client_socket.close()
except KeyboardInterrupt:
    print('\nShutting down server ...')
finally:
    server_socket.close()
    print("Server socket closed.")