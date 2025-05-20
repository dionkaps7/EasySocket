from typing import Callable, Optional
import threading
import socket

class EasySocketPeer(object):
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
                    if not message and self.closed:
                        break
                    self.on_message(message)
                    self.event_messaged.set()
        except Exception:
            self.close()
    
    def close(self):
        if not self.closed:
            self.closed = True

            try:
                self.sock.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass

            try:
                self.sock.close()
            except Exception:
                pass
            
            if self.on_disconnect:
                self.on_disconnect()

    def recv_message(self):
        message = b""

        while True:
            chunk = self.sock.recv(1)
            if not chunk:
                self.close()
                return b""

            message += chunk
            if message.endswith(self.suffix):
                break
        
        return message[:-len(self.suffix)]

    def send_message(self, message: bytes):
        self.sock.send(message + self.suffix)
    
    def wait_message(self):
        self.event_messaged.wait()
