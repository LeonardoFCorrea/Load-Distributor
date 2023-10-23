import socket

server1_address = ("IP SERVIDOR 1", "TIRAS AS ASPAS - PORTA")

def server1():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(server1_address)
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr[0]}")
                data = conn.recv(1024)
                print(f"Received: {data.decode()}")
                conn.send(b"Response from Server 1")

# Inicialização do servidor 1
if __name__ == "__main__":
    server1()