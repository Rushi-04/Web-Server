Simple Python Web Server
This is a minimalist, single-file web server built from scratch in Python using the socket module. It's designed to serve static files and JSON data, demonstrating the fundamental principles of HTTP requests and responses without relying on web frameworks like Flask or Django.

Features
HTTP GET Handling: Responds to HTTP GET requests for specific paths.

Static File Serving: Serves index.html for the root path (/).

JSON API Endpoint: Serves book.json for the /book path, acting as a simple API.

Favicon Support: Correctly handles and serves the favicon.ico file.

Error Handling: Provides appropriate HTTP status codes for various scenarios:

200 OK: For successful requests.

404 Not Found: For files or paths that don't exist.

405 Method Not Allowed: For HTTP methods other than GET.

Connection Management: Uses a try-except block to gracefully handle client connections and a KeyboardInterrupt to shut down the server.

Non-Blocking accept(): Employs settimeout(1) to prevent the server from blocking indefinitely, allowing for a clean shutdown.

Requirements
Python 3.x: This server is written in Python 3.

Required Files: The server expects the following files to be present in the same directory:

index.html

book.json

favicon.ico

NotFound.html (for custom 404 pages)

Setup and Usage
1. File Structure
Ensure your project directory is set up with the following structure:

.
├── main.py
├── index.html
├── book.json
├── favicon.ico
└── NotFound.html
2. Running the Server
To start the server, simply run the main.py script from your terminal:

Bash

python main.py
You'll see a message indicating the server is running:

Bash

Listening on port 8080 ...
3. Accessing Endpoints
Once the server is running, you can access the following endpoints in your web browser or with a tool like curl:

Homepage: http://localhost:8080/

This will serve the content of index.html.

Book API: http://localhost:8080/book

This will serve the JSON content of book.json.

Favicon: http://localhost:8080/favicon.ico

This will serve the favicon.ico file.

404 Not Found: http://localhost:8080/some-other-path

This will return the content of NotFound.html with a 404 status code.

Code Explanation
Core Components
The server's logic is encapsulated in a single main.py file. Here are the key parts:

Socket Setup
Python

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)
server_socket.settimeout(1)
This section initializes a TCP/IP socket, binds it to a specific host and port, and starts listening for incoming connections. The SO_REUSEADDR option allows the socket to be reused immediately after the server is shut down, and settimeout(1) makes the accept() call non-blocking, which is crucial for a clean KeyboardInterrupt.

Main Loop
Python

while True:
    try:
        client_socket, client_address = server_socket.accept()
        # ... request processing ...
    except socket.timeout:
        continue
The server runs in an infinite loop, continuously attempting to accept new client connections. The try...except socket.timeout block ensures the loop doesn't block forever if no clients connect, allowing the KeyboardInterrupt to be detected.

Request Parsing and Response Logic
Python

# Extract the HTTP method and path from the request
http_method, path = first_header_component[0], first_header_component[1]

# Conditional logic to handle different paths and methods
if http_method == 'GET':
    if path == '/':
        # ... serve index.html ...
    elif path == '/book':
        # ... serve book.json ...
    # ... and so on ...
This part of the code reads the incoming HTTP request, extracts the method and the requested path from the first line of the header, and then uses a series of if/elif statements to determine which file to serve.

Sending the Response
Python

client_socket.sendall(response.encode())
Once the response headers and content are generated, they are encoded into bytes and sent back to the client using sendall(). The sendall() method ensures that all the data is sent, which is more reliable than send().

Contributing
This project is a great starting point for understanding network programming in Python. If you want to contribute, feel free to fork the repository and submit a pull request with any improvements or new features.