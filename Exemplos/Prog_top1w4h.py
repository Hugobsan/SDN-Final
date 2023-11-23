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
    print ("*** Criando um comutador")
    s1 = net.addSwitch( 's1' )
    print ("*** Criando host 1")

    h1 = net.addHost('h1')
    print ("*** Criando host 2")
    h2 = net.addHost('h2')
    print ("*** Criando host 3")
    h3 = net.addHost('h3')
    print ("*** Criando host 4")
    h4 = net.addHost('h4')
    print ("*** Criando os enlaces dos hosts para o comutador")
    net.addLink( s1, h1, bw=100, delay='50ms', loss=0, use_htb=True )
    net.addLink( s1, h2, bw=100, delay='50ms', loss=0, use_htb=True )
    net.addLink( s1, h3, bw=100, delay='50ms', loss=0, use_htb=True )
    net.addLink( s1, h4, bw=100, delay='50ms', loss=0, use_htb=True )
    print ("*** Iniciando o rede")
    net.build()
    print ("*** Iniciando o controlador")
    c1.start()
    print ("*** Iniciando o comutado, conectado ao Controlador C1")
    s1.start( [ c1 ] )
    # Iniciando a interface de linha de comando do Mininet
    CLI(net)
    print ("Parando a Simulacao")
    net.stop()

simulaRede()
