# Simple Python Web Server

A **minimalist web server** built from scratch in Python using the `socket` module.  
It serves **static files** and **JSON data**, showcasing the **fundamentals of HTTP requests and responses** without relying on external frameworks.

---

## Features

-  **HTTP GET Handling** → Responds to `GET` requests for specific paths.  
-  **Static File Serving** → Serves `index.html` at `/` and `NotFound.html` for unknown paths.  
-  **JSON API Endpoint** → Provides `book.json` at `/book`.  
-  **Favicon Support** → Correctly handles `/favicon.ico`.  
-  **Robust Error Handling** → Returns proper HTTP status codes:
  -  `200 OK` → Successful requests  
  -  `404 Not Found` → Invalid paths  
  -  `405 Method Not Allowed` → Non-GET methods  
-  **Graceful Shutdown** → Uses `settimeout(1)` to prevent indefinite blocking and enables clean shutdown via **Ctrl + C**.  

---

## Requirements

- **Python 3.x**  
- Required files in the project directory:
  - `index.html`  
  - `book.json`  
  - `favicon.ico`  
  - `NotFound.html`  

---

## Project Structure

```bash
.
├── main.py
├── index.html
├── book.json
├── favicon.ico
└── NotFound.html
```

---

## Usage

###  Run the Server
```bash
python main.py
```

### Access Endpoints
-  **Homepage** → [http://localhost:8080/](http://localhost:8080/)  
  Serves `index.html`  

-  **Book API** → [http://localhost:8080/book](http://localhost:8080/book)  
  Serves `book.json`  

-  **Favicon** → [http://localhost:8080/favicon.ico](http://localhost:8080/favicon.ico)  
  Serves `favicon.ico`  

-  **404 Not Found** → [http://localhost:8080/invalid](http://localhost:8080/invalid)  
  Serves `NotFound.html` with a `404 Not Found` status  

---

##  How It Works

### Socket Setup
- Creates a TCP socket and binds to port `8080`.  
- Uses `SO_REUSEADDR` for immediate reuse after shutdown.  
- `settimeout(1)` ensures the server loop remains responsive.  

###  Request Parsing
- Reads the incoming HTTP request.  
- Extracts the **method** and **path** from the header.  
- Routes requests to the correct file or response logic.  

###  Response Building
- Constructs HTTP headers + body.  
- Sends the response back using `sendall()`.  

---

##  Why This Project?

This project is a **great starting point** for learning:

-  Network programming in Python  
-  How HTTP requests/responses work at a low level  
-  The basics of building your own server  

It can be extended into something bigger:  
-  Add routing logic  
-  Implement `POST`/`PUT` support  
-  Add concurrency with `asyncio` or `ThreadPoolExecutor`  


---

 *“The best way to understand web servers is to build one yourself.”*
