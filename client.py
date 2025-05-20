from typing import Callable, Optional
import threading
import socket


class EasySockClientSocket(object):
    def __init__(self, sock: socket.socket, suffix: bytes):
        self.event_messaged = threading.Event()
        self.closed = False

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
                raise Exception("Unexpectedly disconnected from the server.")
            
            message += chunk
            if message.endswith(self.suffix):
                break
        
        return message.removesuffix(self.suffix)

    def send_message(self, message: bytes):
        self.sock.send(message + self.suffix)

    def wait_message(self):
        self.event_messaged.wait()


class EasySockClient(object):
    def __init__(self, host: str, port: int, on_connect: Callable[[EasySockClientSocket], None], suffix: bytes = b"\x00\x00\x00\x00\x00", timeout: int = None, threaded: bool = False):
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
                threading.Thread(target=self.on_connect, args=[EasySockClientSocket(sock=sock, suffix=self.suffix)], daemon=True).start()
            else:
                self.on_connect(EasySockClientSocket(sock=sock, suffix=self.suffix))
