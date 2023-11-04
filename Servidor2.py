import socket

# Endereço IP e porta do servidor 2
server2_address = ("ENDEREÇO IP", "TIRE AS ASPAS - PORTA")

# Implementação do servidor 2 para receber as solicitações
def server2(log_file):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(server2_address)
        s.listen(1)  # Defina o número máximo de conexões pendentes
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                print("Received: {}".format(data.decode()))  # Use a formatação tradicional
                conn.send(b"Response from Server 2")

                # Registre a métrica
                log_metric = "Server 2, {}, {}".format(addr[0], data.decode())  # Use a formatação tradicional
                log_file.write(log_metric + '\n')

# Inicialização do servidor 2
if __name__ == "__main__":
    log_file_name = "server2_metrics.txt"
    log_file = open(log_file_name, "a")  # Abre o arquivo em modo de adição (append)
    server2(log_file)
    log_file.close()
