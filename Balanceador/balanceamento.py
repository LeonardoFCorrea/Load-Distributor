import socket
import time
import random


vm_addresses = [("192.168.1.210", 3003), ("192.168.1.192", 3003)] # IPs dos servidores


# Função para o algoritmo Round Robin
def round_robin_client():
while True:
address = vm_addresses[random.randint(0, len(vm_addresses) - 1)]


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
s.connect(address)
s.send(b"Round Robin Request")
data = s.recv(1024)
print(f"Round Robin Received from {address[0]}: {data.decode()}")


# Função para o algoritmo Least Response Time
def least_response_time_client():
while True:
response_times = [measure_response_time(addr) for addr in vm_addresses]
min_response_time_index = response_times.index(min(response_times))
address = vm_addresses[min_response_time_index]


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
s.connect(address)
s.send(b"Least Response Time Request")
data = s.recv(1024)
print(f"Least Response Time Received from {address[0]}: {data.decode()}")


# Função para o algoritmo Chained Failover
def chained_failover_client():
while True:
for address in vm_addresses:
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
try:
s.connect(address)
s.send(b"Chained Failover Request")
data = s.recv(1024)
print(f"Chained Failover Received from {address[0]}: {data.decode()}")
break 
except Exception as e:
print(f"Failed to connect to {address[0]}: {e}")
continue


# Função para medir o tempo de resposta
def measure_response_time(vm_address):
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
start_time = time.time()
s.connect(vm_address)
s.send(b"Measure Response Time Request")
data = s.recv(1024)
end_time = time.time()
return end_time - start_time


if __name__ == "__main__":
algorithm_choice = input("Escolha o algoritmo (1 para Round Robin, 2 para Least Response Time, 3 para Chained Failover): ")


if algorithm_choice == "1":
round_robin_client()
elif algorithm_choice == "2":
least_response_time_client()
elif algorithm_choice == "3":
chained_failover_client()
else:
print("Escolha de algoritmo inválida. Use 1, 2 ou 3 para escolher o algoritmo.")