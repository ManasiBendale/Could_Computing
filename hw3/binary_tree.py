from mininet.topo import Topo


class BinaryTreeTopo(Topo):
    "Binary Tree Topology Class."

    def __init__(self):
        "Create the binary tree topology."

        # Initialize topology
        Topo.__init__(self)
        # Add hosts
        h1 = self.addHost('host_h1')
        h2 = self.addHost('host_h2')
        h3 = self.addHost('host_h3')
        h4 = self.addHost('host_h4')
        h5 = self.addHost('host_h5')
        h6 = self.addHost('host_h6')
        h7 = self.addHost('host_h7')
        h8 = self.addHost('host_h8')

        # Add switches
        s1 = self.addSwitch('switch_s1')
        s2 = self.addSwitch('switch_s2')
        s3 = self.addSwitch('switch_s3')
        s4 = self.addSwitch('switch_s4')
        s5 = self.addSwitch('switch_s5')
        s6 = self.addSwitch('switch_s6')
        s7 = self.addSwitch('switch_s7')

        # Add links
        self.addLink(s1, s2)
        self.addlink(s1, s5)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s3, h1)
        self.addLink(s3, h2)
        self.addLink(s4, h3)
        self.addLink(s4, h4)
        self.addLink(s5, s6)
        self.addLink(s5, h7)
        self.addLink(s6, h5)
        self.addLink(s6, h6)
        self.addLink(s7, h7)
        self.addLink(s7, h8)


topos = {'Binary-Tree': (lambda: BinaryTreeTopo())}