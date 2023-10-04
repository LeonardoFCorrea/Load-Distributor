import socket

HOST = '0.0.0.0'  
PORT = 8080      

destinos = ['192.168.1.2', '192.168.1.3']  

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Servidor de balanceamento ouvindo na porta {PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Conexão recebida de {client_address}")
