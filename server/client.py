import socket

host, port = 'localhost', 5555 

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))
print("Client connecté !")

data = "Hi !"
data = data.encode("utf8")
socket.sendall(data)
   
socket.close()