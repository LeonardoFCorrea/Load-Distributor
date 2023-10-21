# Load-Distributor

## Load Balancer with Dynamic Algorithms
This GitHub repository hosts a project that implements a load distributor using three dynamic load balancing algorithms: Round Robin, Chained Failover, and Measure Response Time.

### Round Robin
The Round Robin algorithm evenly distributes incoming requests among a group of servers. It ensures fair utilization of resources but doesn't consider the server's capacity or load.

### Chained Failover
This algorithm forwards requests to the first available server in a list. If that server fails, the request is routed to the next server in the list. It is primarily used for high availability and fault tolerance.

### Measure Response Time
The Measure Response Time algorithm directs requests to the server with the shortest response time, measured from the request's dispatch to the receipt of the response. This helps distribute the load based on the actual performance of the servers.

## Descrição em Português:

## Balanceador de Carga com Algoritmos Dinâmicos
Este repositório no GitHub hospeda um projeto que implementa um distribuidor de carga usando três algoritmos dinâmicos de balanceamento de carga: Round Robin, Chained Failover e Measure Response Time.

### Round Robin
O algoritmo Round Robin distribui de forma equitativa as solicitações de entrada entre um grupo de servidores. Ele garante a utilização justa dos recursos, mas não considera a capacidade ou carga do servidor.

### Chained Failover
Este algoritmo encaminha solicitações para o primeiro servidor disponível em uma lista. Se esse servidor falhar, a solicitação é encaminhada para o próximo servidor da lista. É usado principalmente para alta disponibilidade e tolerância a falhas.

### Measure Response Time
O algoritmo Measure Response Time direciona solicitações para o servidor com o menor tempo de resposta, medido a partir do envio da solicitação até a recepção da resposta. Isso ajuda a distribuir a carga de acordo com o desempenho real dos servidores.
