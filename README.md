# Load-Distributor

## Load Balancer with Dynamic Algorithms
This GitHub repository hosts a project that implements a load distributor using three dynamic load balancing algorithms: Round Robin, Weighted Round Robin, Chained Failover, and Least Response Time.

### Round Robin
The Round Robin algorithm evenly distributes incoming requests among a group of servers. It ensures fair utilization of resources but doesn't consider the server's capacity or load.

### Weighted Round Robin
A variation of Round Robin, the Weighted Round Robin assigns a weight to each server. Servers with higher weights receive more requests compared to those with lower weights. This is beneficial when servers have different capacities, and you want to distribute the load according to their relative capabilities.

### Chained Failover
This algorithm forwards requests to the first available server in a list. If that server fails, the request is routed to the next server in the list. It is primarily used for high availability and fault tolerance.

### Least Response Time
The Least Response Time algorithm directs requests to the server with the shortest response time, measured from the request's dispatch to the receipt of the response. This helps distribute the load based on the actual performance of the servers.

## Descrição em Português:

## Balanceador de Carga com Algoritmos Dinâmicos
Este repositório no GitHub hospeda um projeto que implementa um distribuidor de carga usando três algoritmos dinâmicos de balanceamento de carga: Round Robin, Weighted Round Robin, Chained Failover e Least Response Time.

### Round Robin
O algoritmo Round Robin distribui de forma equitativa as solicitações de entrada entre um grupo de servidores. Ele garante a utilização justa dos recursos, mas não considera a capacidade ou carga do servidor.

### Weighted Round Robin
Uma variação do Round Robin, o Weighted Round Robin atribui um peso a cada servidor. Servidores com pesos mais altos recebem mais solicitações em comparação com os de pesos mais baixos. Isso é útil quando os servidores têm capacidades diferentes e você deseja distribuir a carga de acordo com suas capacidades relativas.

### Chained Failover
Este algoritmo encaminha solicitações para o primeiro servidor disponível em uma lista. Se esse servidor falhar, a solicitação é encaminhada para o próximo servidor da lista. É usado principalmente para alta disponibilidade e tolerância a falhas.

### Least Response Time
O algoritmo Least Response Time direciona solicitações para o servidor com o menor tempo de resposta, medido a partir do envio da solicitação até a recepção da resposta. Isso ajuda a distribuir a carga de acordo com o desempenho real dos servidores.
