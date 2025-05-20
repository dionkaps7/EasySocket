# EasySocket
Effortless Python socket server for quick integration.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Example](#example)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [License](#license)

## Overview
**EasySocketServer** is the easiest possible socket server implementation in Python. It allows you to handle new client connections, messages, and disconnections with clean, Lua-style callbacks.

## Features
- Minimal setup
- Custom `on_connect`, `on_message`, and `on_disconnect` hooks
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

## How It Works
- `EasySocketServer` listens for incoming connections
- When a client connects, your `on_connect` callback runs
- You can assign `on_message` and `on_disconnect` callbacks to each client instance

# Requirements
- Python 3.6+

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

Let me know if you want badges (PyPI, license, version), usage in production, or contributor sections added too.
