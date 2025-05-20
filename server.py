from typing import Callable, Optional
import threading
import socket


class EasySocketServerClient(object):
    event_messaged = threading.Event()
    closed = False

    def __init__(self, sock: socket.socket, suffix: bytes):
        self.sock = sock
        self.suffix = suffix
        self.on_message: Optional[Callable[[bytes], None]] = None
        self.on_disconnect: Optional[Callable[[], None]] = None

        threading.Thread(target=self._listen, daemon=True).start()

    def _listen(self):
        try:
            while True:
                if self.on_message:
                    self.event_messaged.clear()
                    message = self.recv_message()
                    self.on_message(message)
                    self.event_messaged.set()
        except Exception:
            self.closed = True
            
            if self.on_disconnect:
                self.on_disconnect()

    def recv_message(self):
        message = b""

        while True:
            chunk = self.sock.recv(1)
            if not chunk:
                raise Exception("Client disconnected unexpectedly.")

            message += chunk
            if message.endswith(self.suffix):
                break
        
        return message.removesuffix(self.suffix)

    def send_message(self, message: bytes):
        self.sock.send(message + self.suffix)
    
    def wait_message(self):
        self.event_messaged.wait()

class EasySocketServer(object):
    def __init__(self, host: str, port: int, on_connect: Callable[[EasySocketServerClient], None], suffix: bytes = b"\x00\x00\x00\x00\x00"):
        self.host = host
        self.port = port
        self.on_connect = on_connect
        self.suffix = suffix

        threading.Thread(target=self._listen, daemon=True).start()

    def _listen(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock = self.sock
        sock.bind((self.host, self.port))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.listen()

        while True:
            client, _ = sock.accept()

            if self.on_connect:
                threading.Thread(target=self.on_connect, args=[EasySocketServerClient(sock=client, suffix=self.suffix)], daemon=True).start()
