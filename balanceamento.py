import socket
import time
import random

class MetricsLogger:
    def __init__(self, max_logs=3):
        self.max_logs = max_logs
        self.log_count = 0
        self.set_count = 0

    def log_metric(self, log_file, category, algorithm_name, address, start_time, end_time, resource_usage, latency):
        if self.log_count < self.max_logs:
            start_time = round(start_time, 2)
            end_time = round(end_time, 2)
            resource_usage = round(resource_usage, 2)
            latency = round(latency, 2)
            
            metric = "{}: {}, Endereco: {}, Tempo Inicial: {}, Tempo Final: {}, Uso de Recursos: {}, Latencia: {}".format(category, algorithm_name, address[0], start_time, end_time, resource_usage, latency)
            log_file.write(metric + '\n')
            self.log_count += 1
            if self.log_count % 10 == 0:
                self.add_separator_line(log_file)
                self.set_count += 1

    def add_separator_line(self, log_file):
        separator_line = "-" * 300 
        log_file.write(separator_line + '\n')

vm_addresses = [("ENDEREÇO IP", "TIRE AS ASPAS - PORTA"), ("ENDEREÇO IP", "TIRE AS ASPAS - PORTA")]

def measure_response_time(vm_address, request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        start_time = time.time()
        s.connect(vm_address)
        s.send(request.encode())
        data = s.recv(1024)
        end_time = time.time()
        return start_time, end_time

def round_robin_client(log_file, metrics_logger):
    while metrics_logger.log_count < metrics_logger.max_logs:
        address = vm_addresses[random.randint(0, len(vm_addresses) - 1)]
        request = "Round Robin Request"
        start_time, end_time = measure_response_time(address, request)
        resource_usage = random.uniform(0, 1)
        latency = random.uniform(0, 0.5)
        category = "Metrica 1"  # Categoria para Round Robin
        metrics_logger.log_metric(log_file, category, "Round Robin", address, start_time, end_time, resource_usage, latency)
        print("Round Robin Received from {}".format(address[0]))

def least_response_time_client(log_file, metrics_logger):
    while metrics_logger.log_count < metrics_logger.max_logs:  
        response_times = []
        for address in vm_addresses:
            request = "Least Response Time Request"
            start_time, end_time = measure_response_time(address, request)
            response_times.append((start_time, end_time))

        min_response_time_index = response_times.index(min(response_times))
        address = vm_addresses[min_response_time_index]
        start_time, end_time = measure_response_time(address, "Least Response Time Request")
        resource_usage = random.uniform(0, 1) 
        latency = random.uniform(0, 0.5)  
        category = "Metrica 2"  # Categoria para Least Response Time
        metrics_logger.log_metric(log_file, category, "Least Response Time", address, start_time, end_time, resource_usage, latency)
        print("Least Response Time Received from {}".format(address[0]))

def chained_failover_client(log_file, metrics_logger):
    while metrics_logger.log_count < metrics_logger.max_logs:  
        address_order = list(range(len(vm_addresses)))  
        random.shuffle(address_order)  

        for index in address_order:
            address = vm_addresses[index]
            try:
                request = "Chained Failover Request"
                start_time, end_time = measure_response_time(address, request)
                resource_usage = random.uniform(0, 1)  
                latency = random.uniform(0, 0.5)  
                category = "Metrica 3"  # Categoria para Chained Failover
                metrics_logger.log_metric(log_file, category, "Chained Failover", address, start_time, end_time, resource_usage, latency)
                print("Chained Failover Received from {}".format(address[0]))
                break  
            except Exception as e:
                print("Failed to connect to {}: {}".format(address[0], e))
                continue

if __name__ == "__main__":
    log_file_name = "load_distributor_metrics.txt"

    with open(log_file_name, "a") as log_file:

        algorithm_choice = input("Escolha o algoritmo (1 para Round Robin, 2 para Least Response Time, 3 para Chained Failover): ")

        metrics_logger = MetricsLogger()

        if algorithm_choice == "1":
            round_robin_client(log_file, metrics_logger)
        elif algorithm_choice == "2":
            least_response_time_client(log_file, metrics_logger)
        elif algorithm_choice == "3":
            chained_failover_client(log_file, metrics_logger)
        else:
            print("Escolha de algoritmo inválida. Use 1, 2 ou 3 para escolher o algoritmo.")
