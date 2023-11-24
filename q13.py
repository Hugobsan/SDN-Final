# -*- coding: utf-8 -*-
#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel

from os import environ
POXDIR = environ[ 'HOME' ] + '/pox'

#Definindo a classe POX para ser utilizada como controlador
class POX( Controller ):
    def __init__( self, name, cdir=POXDIR, command='python pox.py', cargs=( 'openflow.of_01 --port=%s ' 'forwarding.hub' ), **kwargs ):
        Controller.__init__( self, name, cdir=cdir, command=command, cargs=cargs, **kwargs )

def simulaRede():
    "Criando um ambiente de simulacao mininet"
    net = Mininet( controller=POX, switch=OVSSwitch, link=TCLink )
    print("*** Criando o Controlador na porta 6634")
    c1 = net.addController( 'c1', port=6634 )

    print ("*** Criando switches")
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')

    print ("*** Criando hosts")
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    h5 = net.addHost('h5')

    print ("*** Criando os enlaces dos hosts para o comutador")
    # Adiciona os enlaces entre os switches e os hosts
    net.addLink(h1, s1, bw=100, delay='10ms')
    net.addLink(h2, s2, bw=100, delay='10ms')
    net.addLink(h3, s3, bw=100, delay='10ms')
    net.addLink(h4, s4, bw=100, delay='10ms')
    net.addLink(h5, s5, bw=100, delay='10ms')

    print ("*** Criando os enlaces entre os switches")
    # Conectar os switches
    net.addLink(s1, s5)
    net.addLink(s1, s4)
    net.addLink(s2, s3)
    net.addLink(s2, s5)
    net.addLink(s3, s4)

    print ("*** Iniciando o rede")
    net.build()
    print ("*** Iniciando o controlador")
    c1.start()
    print ("*** Iniciando os comutadores")
    s1.start( [ c1 ] )
    s2.start( [ c1 ] )
    s3.start( [ c1 ] )
    s4.start( [ c1 ] )
    s5.start( [ c1 ] )

    # Configurar os endereços IP para os hosts
    h1.cmd('ifconfig h1-eth0 10.0.0.1 netmask 255.255.255.0')
    h2.cmd('ifconfig h2-eth0 10.0.0.2 netmask 255.255.255.0')
    h3.cmd('ifconfig h3-eth0 10.0.0.3 netmask 255.255.255.0')
    h4.cmd('ifconfig h4-eth0 10.0.0.4 netmask 255.255.255.0')
    h5.cmd('ifconfig h5-eth0 10.0.0.5 netmask 255.255.255.0')
    
    # Iniciando a interface de linha de comando do Mininet
    CLI(net)
    print ("Parando a Simulacao")
    net.stop()

simulaRede()
