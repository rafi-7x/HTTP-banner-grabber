import socket

def grab_banner(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    request = "GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n"
    s.sendall(request.encode())
    banner_bytes = s.recv(1024)
    banner_string = banner_bytes.decode('utf-8')
    banner_list = banner_string.split("\r\n")
    for line in banner_list:
        if line.startswith("Server:"):
            result = line.split(":",1)[1].strip()
            print(f"Server: {result}")
            break
    else:
        print("Not found")
        return 0
host = "127.0.0.1"
port = 8080            
grab_banner(host, port)