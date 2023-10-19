import socket
import time
import random

# Lista de endereços IP das máquinas virtuais de destino
destinos = ['192.168.1.2', '192.168.1.3', '192.168.1.4']  # Substitua pelos IPs reais das máquinas virtuais
destinos_tempo_resposta = {}  # Dicionário para rastrear o tempo de resposta de cada destino

# Porta para encaminhar as solicitações
PORT = 8080

def round_robin():
    current_index = 0

    while True:
        yield destinos[current_index]
        current_index = (current_index + 1) % len(destinos)

def least_response_time():
    while True:
        destinos.sort(key=lambda destino: destinos_tempo_resposta.get(destino, 0))
        yield destinos[0]

def chained_failover():
    current_index = 0

    while True:
        yield destinos[current_index]
        current_index = (current_index + 1) % len(destinos)

def main(method):
    if method == "round-robin":
        dest_selector = round_robin()
    elif method == "least-response-time":
        dest_selector = least_response_time()
    elif method == "chained-failover":
        dest_selector = chained_failover()
    else:
        raise ValueError("Método de balanceamento de carga desconhecido")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', PORT))
    server_socket.listen(5)

    print(f"Servidor de balanceamento ({method}) ouvindo na porta {PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexão recebida de {client_address}")

        try:
            destino_atual = next(dest_selector)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as destino_socket:
                start_time = time.time()
                destino_socket.connect((destino_atual, PORT))
                data = client_socket.recv(1024)
                destino_socket.sendall(data)
                response = destino_socket.recv(1024)
                client_socket.sendall(response)
                end_time = time.time()
                tempo_resposta = end_time - start_time
                destinos_tempo_resposta[destino_atual] = tempo_resposta

        except Exception as e:
            print(f"Erro ao encaminhar a solicitação: {e}")

        client_socket.close()

if __name__ == "__main__":
    print("Escolha o método de balanceamento de carga:")
    print("1. Round Robin")
    print("2. Least Response Time")
    print("3. Chained Failover")

    escolha = input("Digite o número do método desejado: ")

    if escolha == "1":
        metodo_balanceamento = "round-robin"
    elif escolha == "2":
        metodo_balanceamento = "least-response-time"
    elif escolha == "3":
        metodo_balanceamento = "chained-failover"
    else:
        print("Método de balanceamento de carga inválido.")
        sys.exit(1)

    main(metodo_balanceamento)