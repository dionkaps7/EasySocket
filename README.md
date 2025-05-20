# EasySocket
Effortless Python socket server for quick integration.

# Examples
## Server
```python
from peer import EasySocketPeer
from server import EasySocketServer

def on_connect(sock_client: EasySocketPeer):
    client_address = sock_client.sock.getpeername()
    print(f"Connected: {client_address}")

    def on_message(data: bytes):
        print(f"Received ({client_address}): {data}")
        sock_client.send_message(b"Acknowledged: " + data)
    
    def on_disconnect():
        print(f"Disconnected: {client_address}")

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

## Client
```python
from peer import EasySocketPeer
from client import EasySocketClient

def on_connect(sock: EasySocketPeer):
    print(f"Connected to server: {sock.sock.getpeername()}")

    def on_message(message: bytes):
        print(f"Message from the server: {message}")

    def on_disconnect():
        print(f"Disconnected from the server.")

    sock.sock.settimeout(None)
    sock.on_message = on_message
    sock.on_disconnect = on_disconnect

    while True:
        if sock.closed:
            break

        message = input("Send message: ")

        if sock.closed:
            break

        sock.send_message(message=message.encode())
        sock.wait_message()

def main():
    host = "127.0.0.1"
    port = 4444

    client = EasySocketClient(host=host, port=port, on_connect=on_connect, timeout=10, threaded=False)

if __name__ == "__main__":
    main()
```

# License
```
MIT License

Copyright (c) 2025 ₱ØⱠɎ₥ØⱤ₱Ⱨł₵

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
