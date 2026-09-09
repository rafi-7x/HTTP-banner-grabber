# Simple HTTP Banner Grabber

A lightweight Python utility designed for basic network reconnaissance. It uses raw TCP sockets to establish a connection with a target server, send an HTTP request, and extract the server's identity banner from the response headers.

### Features
* **Zero Dependencies:** Built entirely with Python's standard `socket` module.
* **Header Extraction:** Parses HTTP response headers specifically for the `Server` field.
* **Minimal & Fast:** Ideal for understanding low-level socket communication and server identification.

### How It Works
1. Connects to the designated host and port via a TCP socket.
2. Transmits a standard `GET / HTTP/1.1` request.
3. Decodes the response and searches line-by-line for the `Server:` header.
4. Displays the detected server software string in the terminal.
