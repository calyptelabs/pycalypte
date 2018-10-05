from calypte.calypte_connection import ClaypteConnection;
from socket import socket;

class CalypteConnectionImp(ClaypteConnection):
    
    def __init__(self, host, port):
        self.host = host;
        self.port = port;
        self.sock     = socket.socket(
                            socket.AF_INET, 
                            socket.SOCK_STREAM);
        self.sock.connect((self.host, self.port));
    