# EasySocket
Effortless Python socket server for quick integration.

# EasySocketServer
**EasySocketServer** is the easiest possible socket server implementation in Python. It allows you to handle new client connections, messages, and disconnections with clean, Lua-style callbacks.

## Features
- Minimal setup
- Custom on_connect, on_message, and on_disconnect hooks
- Easy-to-use wrapper for each client socket

## Example
```python
from server import EasySocketServer, EasySocketServerClient

def on_connect(sock_client: EasySocketServerClient):
    print(f"Connected: {sock_client.sock.getpeername()}")

    def on_message(data: bytes):
        print(f"Received ({sock_client.sock.getpeername()}): {data}")
    
    def on_disconnect():
        print(f"Disconnected: {sock_client.sock.getpeername()}")

    sock_client.on_message = on_message
    sock_client.on_disconnect = on_disconnect

def main():
    host = "0.0.0.0"
    port = 4444
    server = EasySocketServer(host=host, port=port, on_connect=on_connect)
    
    print(f"Listening to {host}:{port}...")
    input()

if __name__ == "__main__":
    main()
```
