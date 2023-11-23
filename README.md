# SDN-Final
Repositório para arquivos de configuração de simulação de Redes Definidas por Software (SDN) com Mininet para o projeto final da disciplina de Sistemas Distribuídos I

# O que é uma SDN
O controlador SDN é o cérebro da rede. Ele toma decisões sobre como o tráfego deve ser encaminhado com base em políticas definidas pelo administrador da rede. O controlador se comunica com os dispositivos de rede (switches, roteadores, etc.) usando protocolos como o OpenFlow, que permite que o controlador instrua os dispositivos sobre como encaminhar pacotes.
Nas redes tradicionais com arquitetura integrada, os planos de dados e controle coexistem nos mesmos dispositivos, como roteadores e switches. Isso proporciona simplicidade, mas pode dificultar a escalabilidade e a flexibilidade. Em contraste, em uma SDN, coloca-se o controle em um controlador centralizado, permitindo escalabilidade e flexibilidade.

# O que é o Mininet
O Mininet é um emulador de rede que cria redes com servidores, switches, controladores e enlaces virtuais.

# Como utilizar do projeto
## 1 - Configuração do ambiente
Primeiramente, é necessário configurar o ambiente virtual. Para o desenvolvimento, foi utilizado o VirtualBox, com uma imagem Linux pré-configurada com todas as dependências, incluindo o Mininet. 
Para configurar o ambiente, recomendo seguir o tutorial: https://pradeepaphd.wordpress.com/2016/07/12/install-all-sdn-controllers-from-sdn-hub/. Foi utilizado a versão de 32 bits do OVA, portanto, não foi testada a possibilidade de funcionar no 64 bits.
Após seguir o tutorial, seu ambiente está configurado e pronto para uso.

## 2 - Utilização da rede configurada
Após configurar o ambiente. Faça download dos códigos python para o ambiente virtual.
Com eles separados em uma pasta, abra o terminal e inicialize a rede com o comando:
```
sudo python nome_do_arquivo.py
```

Por exemplo, caso queira abrir a rede configurada no arquivo *Prog_top1w4h.py*, use o comando:
```
sudo python Prog_top1w4h.pye
```

Após isso, a rede irá ser criada, e o terminal passará a ser uma instância do mininet, simulando a rede pré-configurada no código python.

Abaixo, seguem alguns comandos para gerir a rede:

**Verificar os nós da rede**
``` 
nodes 
```
**Verificar os enlaces da rede**
```
net
```

**Verificar a configuração de endereços IP dos dispositivos da rede**
```
dump
```

**Acessar o terminal de determinados dispositivos**
```
xterm nome
```

Exemplo: 
```
xterm h1 h4
```
*Esse comando irá abrir os terminais do host 1 e host 4*

***COMANDOS PARA O TERMINAL DOS HOSTS***

**Teste de conectividade da rede**
```
ping ip_destino -concentrador
```

*Exemplo de ping para o host 10.0.0.1 através do concentrador c1*

```
ping 10.0.0.1 -c1
```

**Testando o iperf**

**1 - Escolha um host como servidor**
No exemplo, será h6 (10.0.0.6). Dentro do terminal do h6, dê o comando:
```
iperf -s
```
Isso manterá o h6 ouvindo, como servidor.

**2 - Escolha um host como cliente**
No exemplo, será o h1. O h1 fará uma requisição ao h6 com o iperf. Através disso, algumas métricas da rede serão visualizada. Para fazer a requisição ao h6, o comando será:

```
iperf -c 10.0.0.6
```

** Saindo do mininet **
Para sair dos terminais dos hosts, basta fechá-los.
Para sair do mininet no terminal principal, execute o comando:

```
exit
```

Após sair, dê o comando abaixo para limpar a memória da rede e evitar erros futuros:
```
sudo mn -c 
```