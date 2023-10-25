import socket

# Endereço IP e porta do servidor 1
server1_address = ("ENDEREÇO IP", "TIRE AS ASPAS - PORTA")

# Implementação do servidor 1 para receber as solicitações
def server1(log_file):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(server1_address)
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                print(f"Received: {data.decode()}")
                conn.send(b"Response from Server 1")

                # Registre a métrica
                log_metric = f"Server 1,{addr[0]},{data.decode()}"
                log_file.write(log_metric + '\n')

# Inicialização do servidor 1
if __name__ == "__main__":
    log_file_name = "server1_metrics.txt"
    log_file = open(log_file_name, "a")  # Abre o arquivo em modo de adição (append)
    server1(log_file)
    log_file.close()