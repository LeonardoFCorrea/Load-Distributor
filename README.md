# Guia Técnico para o Load-Distributor

## Cliente:

O código do cliente é responsável por se comunicar com servidores e realizar três tipos de distribuição de carga: Round Robin (Rodízio), Least Response Time (Menor Tempo de Resposta) e Chained Failover (Falha Encadeada).

* Round Robin (Rodízio): Neste método, o cliente escolhe aleatoriamente um dos servidores disponíveis para enviar a solicitação. A cada solicitação, um servidor diferente é escolhido. Isso garante que as solicitações sejam distribuídas igualmente entre os servidores.

* Measure Response Time (Menor Tempo de Resposta): Aqui, o cliente mede o tempo de resposta de cada servidor disponível. Ele escolhe o servidor com o menor tempo de resposta para enviar a solicitação. Isso ajuda a direcionar as solicitações para o servidor mais rápido.

* Chained Failover (Falha Encadeada): Neste método, o cliente tenta se conectar a cada servidor na lista. Se a conexão falhar, ele tenta o próximo servidor. Quando uma conexão bem-sucedida é estabelecida, a solicitação é enviada. Isso é útil quando você deseja uma abordagem de failover, na qual os servidores são usados na ordem até que um funcione.

## Servidores:

Os códigos dos servidores representam os servidores que respondem às solicitações do cliente. Cada servidor possui um endereço IP e uma porta específica na qual ele "escuta" as solicitações do cliente. Os servidores respondem com uma mensagem "Response from Server X", onde X representa o número do servidor.

* Server 1: Este é o primeiro servidor com o endereço IP definido e a porta especificada. Ele está configurado para responder a solicitações do cliente e mostrar uma mensagem quando uma solicitação é recebida.

* Server 2: Este é o segundo servidor com o endereço IP definido e a porta especificada. Assim como o Server 1, ele também está configurado para responder a solicitações do cliente e mostrar uma mensagem quando uma solicitação é recebida.

## Requisitos:

* Duas máquinas, uma para o cliente e duas para os servidores.
* Python instalado nas máquinas.

## Passo 1: Configuração dos IPs e Portas:

Abra o código do cliente e defina os IPs e portas dos servidores. Substitua "IP SERVIDOR 1" e "IP SERVIDOR 2" pelas informações reais dos servidores. Certifique-se de que as portas estão disponíveis e podem ser usadas.
Faça o mesmo nos códigos dos servidores, substituindo "IP DO SERVIDOR 1" e "IP DO SERVIDOR 2" pelos endereços IP corretos.

## Passo 2: Executando os Servidores:

Nas máquinas que atuarão como servidores, abra os códigos "server1.py" e "server2.py" com Python. Isso iniciará os servidores que aguardarão as solicitações do cliente.
Certifique-se de que as portas especificadas nos servidores correspondam às portas definidas no cliente.
## Passo 3: Executando o Cliente:

Na máquina que atuará como cliente, execute o código do cliente, "client.py", com Python.
O cliente permitirá que você escolha entre três algoritmos de distribuição de carga: Round Robin (1), Least Response Time (2) e Chained Failover (3).

## Passo 4: Escolhendo um Algoritmo:

Digite o número correspondente ao algoritmo que deseja testar e pressione "Enter". O cliente começará a enviar solicitações aos servidores com base no algoritmo escolhido.

## Passo 5: Observando a Distribuição de Carga:

Os servidores responderão às solicitações do cliente e mostrarão mensagens indicando que receberam as solicitações.
No cliente, você verá as respostas dos servidores, indicando de qual servidor a resposta foi recebida.

Observações:

* Certifique-se de que as máquinas com endereços IP de servidor possam ser acessadas a partir de computadores clientes. 
* Você pode executar os algoritmos quantas vezes quiser, escolhendo diferentes algoritmos para ver como a distribuição de carga é afetada.
* Este guia técnico fornece uma visão geral de como configurar e usar código para testar algoritmos de balanceamento de carga. Certifique-se de compreender as configurações de IP e porta e a seleção do algoritmo para obter resultados precisos.

