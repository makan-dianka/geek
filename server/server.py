import socket

host, port = '', 5555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Le server est démarré ...")

while True:
    socket.listen(5)
    conn, adresse = socket.accept()
    print(f"\nSocket connecté: {adresse}:{port}  message:")
    
    data = conn.recv(1024)
    data = data.decode("utf8")
    print(data)
    
    
conn.close()
socket.close()
  