# -*- coding: utf-8 -*-
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.cli import CLI
from mininet.log import setLogLevel

#printar a topologia da rede no terminal
#sudo mn --custom principal.py --topo mytopo --test pingall


# Criar a rede
def create_network():
    net = Mininet(controller=Controller, switch=OVSSwitch)
    
    # Adicionar o controlador
    c0 = net.addController('c0')

    # Adicionar as switches
    switches = {}
    
    for i in range(1, 6):
        switches['s%s' % i] = net.addSwitch('s%s' % i)

    # Adiciona os hosts à rede
    hosts = {}

    for i in range(1, 11):
        hosts['h%s' % i] = net.addHost('h%s' % i)

    # Adiciona os enlaces entre os switches e os hosts dividindo igualmente entre os switches

    for i in range(1, 6):
        #Para cada switch, adiciona 2 hosts
        for j in range(1, 3):
            net.addLink(switches['s%s' % i], hosts['h%s' % j])
        

    # Conectar os switches
    net.addLink(switches['s1'], switches['s5'])
    net.addLink(switches['s1'], switches['s4'])
    net.addLink(switches['s2'], switches['s3'])
    net.addLink(switches['s2'], switches['s5'])
    net.addLink(switches['s3'], switches['s4'])

    # Iniciar a rede
    net.build()
    c0.start()

    # Iniciar as switches com o controlador
    for i in range(1, 6):
        switches['s%s' % i].start([c0])

    # Configurar os endereços IP para os hosts
    for i in range(1, 11):
        hosts['h%s' % i].cmd('ifconfig h%s-eth0 10.0.0.%s netmask 255.255.255.0' % (i, i))
    
    # Definir o controlador para as switches
    for i in range(1, 6):
        switches['s%s' % i].cmd('ovs-vsctl set Bridge s%s protocols=OpenFlow13' % i)
        
    # Iniciar a interface de linha de comando
    CLI(net)

    # Parar a rede
    net.stop()

if(__name__ == '__main__'):
    setLogLevel('info')
    create_network()
