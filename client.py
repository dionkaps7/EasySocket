from peer import EasySocketPeer
from typing import Callable
import threading
import socket


class EasySocketClient(object):
    def __init__(self, host: str, port: int, on_connect: Callable[[EasySocketPeer], None], suffix: bytes = b"\x00\x00\x00\x00\x00", timeout: int = None, threaded: bool = False):
        self.host = host
        self.port = port
        self.on_connect = on_connect
        self.suffix = suffix
        self.timeout = timeout
        self.threaded = threaded

        if threaded:
            threading.Thread(target=self._connect, daemon=True).start()
        else:
            self._connect()
    
    def _connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.timeout)
        sock.connect((self.host, self.port))

        if self.on_connect:
            if self.threaded:
                threading.Thread(target=self.on_connect, args=[EasySocketPeer(sock=sock, suffix=self.suffix)], daemon=True).start()
            else:
                self.on_connect(EasySocketPeer(sock=sock, suffix=self.suffix))
