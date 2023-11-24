# -*- coding: utf-8 -*-
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel

# Criar a rede
def create_network():
    net = Mininet(controller=Controller, switch=OVSSwitch)
    
    # Adicionar o controlador
    c0 = net.addController('c0')

    # Adicionar as switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')

    # Adiciona os hosts à rede
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    h5 = net.addHost('h5')

    # Adiciona os enlaces entre os switches e os hosts
    net.addLink(h1, s1, cls=TCLink, bw=100, delay='10ms')
    net.addLink(h2, s2, cls=TCLink, bw=100, delay='10ms')
    net.addLink(h3, s3, cls=TCLink, bw=100, delay='10ms')
    net.addLink(h4, s4, cls=TCLink, bw=100, delay='10ms')
    net.addLink(h5, s5, cls=TCLink, bw=100, delay='10ms')

    # Conectar os switches
    net.addLink(s1, s5)
    net.addLink(s1, s4)
    net.addLink(s2, s3)
    net.addLink(s2, s5)
    net.addLink(s3, s4)

    # Iniciar a rede
    net.build()
    c0.start()

    # Iniciar os switches
    s1.start([c0])
    s2.start([c0])
    s3.start([c0])
    s4.start([c0])
    s5.start([c0])

    # Configurar os endereços IP para os hosts
    h1.cmd('ifconfig h1-eth0 10.0.0.1 netmask 255.255.255.0')
    h2.cmd('ifconfig h2-eth0 10.0.0.2 netmask 255.255.255.0')
    h3.cmd('ifconfig h3-eth0 10.0.0.3 netmask 255.255.255.0')
    h4.cmd('ifconfig h4-eth0 10.0.0.4 netmask 255.255.255.0')
    h5.cmd('ifconfig h5-eth0 10.0.0.5 netmask 255.255.255.0')
    
    # Definir o controlador para as switches
    s1.cmd('ovs-vsctl set-controller s1 tcp:127.0.0.1:6633 protocols=OpenFlow10')
    s2.cmd('ovs-vsctl set-controller s2 tcp:127.0.0.1:6633 protocols=OpenFlow10')
    s3.cmd('ovs-vsctl set-controller s3 tcp:127.0.0.1:6633 protocols=OpenFlow10')
    s4.cmd('ovs-vsctl set-controller s3 tcp:127.0.0.1:6633 protocols=OpenFlow10')
    s5.cmd('ovs-vsctl set-controller s3 tcp:127.0.0.1:6633 protocols=OpenFlow10')
    
    # Iniciar a interface de linha de comando
    CLI(net)

    # Parar a rede
    net.stop()

if(__name__ == '__main__'):
    setLogLevel('info')
    create_network()
