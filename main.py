import socket
import os
import sys
import random
from tqdm import tqdm
import time

class FileTransfert:    
    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 80
        self.server_socket = self.host, self.port
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.bind(self.server_socket)
        self.conn.listen(2)
        print(f"\nsocket ouvert: {self.host}:{self.port}\nserver en ecoute...")

        while True:
            client_socket, client_addr = self.conn.accept()
            print(f"[+] {client_addr[0]}:{client_addr[1]} est connecté")
            
            filename = "<h1> Bonjour Makan  </h1>".encode("utf-8")
            client_socket.sendall(filename)
            
obj = FileTransfert()