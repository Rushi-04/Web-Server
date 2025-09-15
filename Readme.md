🖥️ Python Socket Web Server

A simple HTTP server built from scratch using Python’s socket module.
This project demonstrates the fundamentals of how web servers work internally, without relying on frameworks like Flask or Django.

🚀 Features

Serves static files:

index.html → when visiting /

book.json → when visiting /book

favicon.ico → when browsers request site icon

Handles HTTP response codes:

200 OK → for successful responses

404 Not Found → if a file doesn’t exist

405 Method Not Allowed → for unsupported methods

Graceful shutdown with Ctrl + C

Basic request logging (shows HTTP request in console)

Custom NotFound.html page if available

📂 Project Structure
.
├── main.py          # The server code
├── index.html       # Homepage (served at '/')
├── book.json        # Example JSON response (served at '/book')
├── favicon.ico      # Browser icon (served automatically)
└── NotFound.html    # Optional custom 404 page

⚙️ How It Works

Listens on 0.0.0.0:8080 (all network interfaces, port 8080).

Accepts incoming TCP connections from clients (like browsers).

Parses the HTTP request line (method, path, version).

Serves content depending on the requested path.

Sends an HTTP response back to the client with proper headers and body.

▶️ Running the Server
# Clone this repo or copy the code
python main.py


Then, open your browser and visit:

http://localhost:8080/
 → serves index.html

http://localhost:8080/book
 → serves book.json

Any invalid path → serves NotFound.html (if exists) or plain 404

🛑 Stopping the Server

Press Ctrl + C in the terminal:

Shutting down server ...
Server socket closed.

🎯 Why This Project Matters

Most developers rely on high-level frameworks, but here you implemented:

Raw TCP socket programming

HTTP request/response parsing

Static file serving logic

Error handling & graceful shutdown

This shows a deep understanding of how the web works under the hood.

🔮 Possible Improvements

Add concurrency (ThreadPool or asyncio) for handling multiple clients.

Support POST requests and form submissions.

Serve files from a static/ folder automatically.

Add logging with timestamps and response codes.

Build a simple router (like Flask) for cleaner path handling.

✨ With this project, you’ve basically written a mini Flask clone from scratch!