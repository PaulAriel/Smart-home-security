from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI

net = Mininet(controller=RemoteController)

print("*** Création du contrôleur")
c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)

print("*** Création des hôtes")
h1 = net.addHost('h1', ip='10.0.0.1/24')
h2 = net.addHost('h2', ip='10.0.0.2/24')
h3 = net.addHost('h3', ip='10.0.0.3/24')

print("*** Création du switch")
s1 = net.addSwitch('s1', protocols='OpenFlow13')

print("*** Création des liens")
net.addLink(h1, s1)
net.addLink(h2, s1)
net.addLink(h3, s1)

print("*** Démarrage du réseau")
net.start()

print("*** Test de connectivité")
net.pingAll()

CLI(net)

net.stop()
