# -*- coding: utf-8 -*-
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_network():
    net = Mininet(controller=Controller, switch=OVSSwitch)

    # Adicionar o controlador
    c0 = net.addController('c0')

    # Adicionar as switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    # Adicionar os hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')

    # Conectar hosts às switches
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s2)

    # Conectar switches
    net.addLink(s1, s2)

    # Iniciar a rede
    net.build()
    c0.start()
    s1.start([c0])
    s2.start([c0])

    # Configurar os endereços IP para os hosts
    h1.cmd('ifconfig h1-eth0 10.0.0.1 netmask 255.255.255.0')
    h2.cmd('ifconfig h2-eth0 10.0.0.2 netmask 255.255.255.0')
    h3.cmd('ifconfig h3-eth0 10.0.0.3 netmask 255.255.255.0')
    h4.cmd('ifconfig h4-eth0 10.0.0.4 netmask 255.255.255.0')

    # Definir o controlador para as switches
    s1.cmd('ovs-vsctl set-controller s1 tcp:127.0.0.1:6633')
    s2.cmd('ovs-vsctl set-controller s2 tcp:127.0.0.1:6633')

    # Iniciar a interface de linha de comando
    CLI(net)

    # Parar a rede
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()