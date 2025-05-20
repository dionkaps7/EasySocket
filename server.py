from peer import EasySocketPeer
from typing import Callable
import threading
import socket


class EasySocketServer(object):
    def __init__(self, host: str, port: int, on_connect: Callable[[EasySocketPeer], None], suffix: bytes = b"\x00\x00\x00\x00\x00"):
        self.host = host
        self.port = port
        self.on_connect = on_connect
        self.suffix = suffix

        threading.Thread(target=self._listen, daemon=True).start()

    def _listen(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock = self.sock
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))
        sock.listen()

        while True:
            client, _ = sock.accept()

            if self.on_connect:
                threading.Thread(target=self.on_connect, args=[EasySocketPeer(sock=client, suffix=self.suffix)], daemon=True).start()
