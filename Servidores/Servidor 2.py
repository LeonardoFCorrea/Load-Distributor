import socket

server2_address = ("IP DO SERVIDOR 2", "TIRAR AS ASPAS - PORTA")

def server2():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(server2_address)
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr[0]}")
                data = conn.recv(1024)
                print(f"Received: {data.decode()}")
                conn.send(b"Response from Server 2")

# Inicialização do servidor 2
if __name__ == "__main__":
    server2()