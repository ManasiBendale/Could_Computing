TASK - 1

1. What is the output of “nodes” and “net”
ANS - 
nodes ->
mininet> nodes
available nodes are: 
c0 h1 h2 h3 h4 h5 h6 h7 h8 s1 s2 s3 s4 s5 s6 s7

net ->
mininet> net
h1 h1-eth0:s3-eth1
h2 h2-eth0:s3-eth2
h3 h3-eth0:s4-eth1
h4 h4-eth0:s4-eth2
h5 h5-eth0:s6-eth1
h6 h6-eth0:s6-eth2
h7 h7-eth0:s7-eth1
h8 h8-eth0:s7-eth2
s1 lo:  s1-eth1:s2-eth3 s1-eth2:s5-eth3
s2 lo:  s2-eth1:s3-eth3 s2-eth2:s4-eth3 s2-eth3:s1-eth1
s3 lo:  s3-eth1:h1-eth0 s3-eth2:h2-eth0 s3-eth3:s2-eth1
s4 lo:  s4-eth1:h3-eth0 s4-eth2:h4-eth0 s4-eth3:s2-eth2
s5 lo:  s5-eth1:s6-eth3 s5-eth2:s7-eth3 s5-eth3:s1-eth2
s6 lo:  s6-eth1:h5-eth0 s6-eth2:h6-eth0 s6-eth3:s5-eth1
s7 lo:  s7-eth1:h7-eth0 s7-eth2:h8-eth0 s7-eth3:s5-eth2
c0

2. What is the output of “h7 ifconfig ?
ANS - 
mininet> h7 ifconfig
h7-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.7  netmask 255.0.0.0  broadcast 10.255.255.255
        inet6 fe80::c4d3:19ff:fea2:9f  prefixlen 64  scopeid 0x20<link>
        ether c6:d3:19:a2:00:9f  txqueuelen 1000  (Ethernet)
        RX packets 57  bytes 4410 (4.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 10  bytes 796 (796.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

mininet> 
mininet> 

TASK - 2

1. Draw the function call graph of this controller. For example, once a packet comes to the
controller, which function is the first to be called, which one is the second, and so forth?
ANS - 

Function call graph:
start switch : _handle_PacketIn() -> act_like_hub() -> resend_packet() -> send(msg)

        packet comes in
	
        |
        V
	,__________________,
	|                  |
	| _handle_PacketIn |
	|__________________|
	
	    |
	    V
	,__________________,
	|                  |
	|   act_like_hub   |   (or act_like_switch, once we implement it)
	|__________________|
	
	    |
	    V
	,__________________,
	|                  |
	|  resend_packet   |
	|__________________|
		
	    |
	    V

     forward message to the port
     
2. Have h1 ping h2, and h1 ping h8 for 100 times (e.g., h1 ping -c100 p2).
ANS - 
For h1 ping -c100 h2
mininet> h1 ping -c100 h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=4.52 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=4.26 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=4.23 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=4.25 ms
64 bytes from 10.0.0.2: icmp_seq=5 ttl=64 time=3.52 ms
64 bytes from 10.0.0.2: icmp_seq=6 ttl=64 time=4.33 ms
64 bytes from 10.0.0.2: icmp_seq=7 ttl=64 time=4.17 ms
64 bytes from 10.0.0.2: icmp_seq=8 ttl=64 time=4.60 ms
64 bytes from 10.0.0.2: icmp_seq=9 ttl=64 time=1.65 ms
64 bytes from 10.0.0.2: icmp_seq=10 ttl=64 time=4.03 ms
64 bytes from 10.0.0.2: icmp_seq=11 ttl=64 time=4.10 ms
64 bytes from 10.0.0.2: icmp_seq=12 ttl=64 time=3.75 ms
64 bytes from 10.0.0.2: icmp_seq=13 ttl=64 time=3.80 ms
64 bytes from 10.0.0.2: icmp_seq=14 ttl=64 time=4.00 ms
64 bytes from 10.0.0.2: icmp_seq=15 ttl=64 time=4.21 ms
64 bytes from 10.0.0.2: icmp_seq=16 ttl=64 time=4.36 ms
64 bytes from 10.0.0.2: icmp_seq=17 ttl=64 time=4.16 ms
64 bytes from 10.0.0.2: icmp_seq=18 ttl=64 time=4.29 ms
64 bytes from 10.0.0.2: icmp_seq=19 ttl=64 time=3.88 ms
64 bytes from 10.0.0.2: icmp_seq=20 ttl=64 time=3.63 ms
64 bytes from 10.0.0.2: icmp_seq=21 ttl=64 time=4.31 ms
64 bytes from 10.0.0.2: icmp_seq=22 ttl=64 time=3.73 ms
64 bytes from 10.0.0.2: icmp_seq=23 ttl=64 time=3.58 ms
64 bytes from 10.0.0.2: icmp_seq=24 ttl=64 time=3.62 ms
64 bytes from 10.0.0.2: icmp_seq=25 ttl=64 time=3.63 ms
64 bytes from 10.0.0.2: icmp_seq=26 ttl=64 time=4.44 ms
64 bytes from 10.0.0.2: icmp_seq=27 ttl=64 time=3.63 ms
64 bytes from 10.0.0.2: icmp_seq=28 ttl=64 time=3.52 ms
64 bytes from 10.0.0.2: icmp_seq=29 ttl=64 time=3.64 ms
64 bytes from 10.0.0.2: icmp_seq=30 ttl=64 time=3.97 ms
64 bytes from 10.0.0.2: icmp_seq=31 ttl=64 time=4.78 ms
64 bytes from 10.0.0.2: icmp_seq=32 ttl=64 time=4.01 ms
64 bytes from 10.0.0.2: icmp_seq=33 ttl=64 time=4.29 ms
64 bytes from 10.0.0.2: icmp_seq=34 ttl=64 time=4.25 ms
64 bytes from 10.0.0.2: icmp_seq=35 ttl=64 time=4.31 ms
64 bytes from 10.0.0.2: icmp_seq=36 ttl=64 time=4.30 ms
64 bytes from 10.0.0.2: icmp_seq=37 ttl=64 time=4.18 ms
64 bytes from 10.0.0.2: icmp_seq=38 ttl=64 time=4.21 ms
64 bytes from 10.0.0.2: icmp_seq=39 ttl=64 time=4.09 ms
64 bytes from 10.0.0.2: icmp_seq=40 ttl=64 time=4.22 ms
64 bytes from 10.0.0.2: icmp_seq=41 ttl=64 time=4.03 ms
64 bytes from 10.0.0.2: icmp_seq=42 ttl=64 time=3.94 ms
64 bytes from 10.0.0.2: icmp_seq=43 ttl=64 time=3.85 ms
64 bytes from 10.0.0.2: icmp_seq=44 ttl=64 time=4.21 ms
64 bytes from 10.0.0.2: icmp_seq=45 ttl=64 time=4.05 ms
64 bytes from 10.0.0.2: icmp_seq=46 ttl=64 time=3.98 ms
64 bytes from 10.0.0.2: icmp_seq=47 ttl=64 time=4.20 ms
64 bytes from 10.0.0.2: icmp_seq=48 ttl=64 time=4.20 ms
64 bytes from 10.0.0.2: icmp_seq=49 ttl=64 time=3.82 ms
64 bytes from 10.0.0.2: icmp_seq=50 ttl=64 time=4.62 ms
64 bytes from 10.0.0.2: icmp_seq=51 ttl=64 time=4.52 ms
64 bytes from 10.0.0.2: icmp_seq=52 ttl=64 time=4.46 ms
64 bytes from 10.0.0.2: icmp_seq=53 ttl=64 time=4.52 ms
64 bytes from 10.0.0.2: icmp_seq=54 ttl=64 time=3.94 ms
64 bytes from 10.0.0.2: icmp_seq=55 ttl=64 time=4.74 ms
64 bytes from 10.0.0.2: icmp_seq=56 ttl=64 time=4.36 ms
64 bytes from 10.0.0.2: icmp_seq=57 ttl=64 time=4.54 ms
64 bytes from 10.0.0.2: icmp_seq=58 ttl=64 time=4.27 ms
64 bytes from 10.0.0.2: icmp_seq=59 ttl=64 time=4.22 ms
64 bytes from 10.0.0.2: icmp_seq=60 ttl=64 time=4.47 ms
64 bytes from 10.0.0.2: icmp_seq=61 ttl=64 time=4.29 ms
64 bytes from 10.0.0.2: icmp_seq=62 ttl=64 time=4.23 ms
64 bytes from 10.0.0.2: icmp_seq=63 ttl=64 time=4.23 ms
64 bytes from 10.0.0.2: icmp_seq=64 ttl=64 time=4.20 ms
64 bytes from 10.0.0.2: icmp_seq=65 ttl=64 time=4.12 ms
64 bytes from 10.0.0.2: icmp_seq=66 ttl=64 time=4.09 ms
64 bytes from 10.0.0.2: icmp_seq=67 ttl=64 time=3.97 ms
64 bytes from 10.0.0.2: icmp_seq=68 ttl=64 time=4.12 ms
64 bytes from 10.0.0.2: icmp_seq=69 ttl=64 time=3.99 ms
64 bytes from 10.0.0.2: icmp_seq=70 ttl=64 time=4.80 ms
64 bytes from 10.0.0.2: icmp_seq=71 ttl=64 time=4.48 ms
64 bytes from 10.0.0.2: icmp_seq=72 ttl=64 time=3.56 ms
64 bytes from 10.0.0.2: icmp_seq=73 ttl=64 time=4.49 ms
64 bytes from 10.0.0.2: icmp_seq=74 ttl=64 time=3.97 ms
64 bytes from 10.0.0.2: icmp_seq=75 ttl=64 time=4.57 ms
64 bytes from 10.0.0.2: icmp_seq=76 ttl=64 time=4.79 ms
64 bytes from 10.0.0.2: icmp_seq=77 ttl=64 time=3.53 ms
64 bytes from 10.0.0.2: icmp_seq=78 ttl=64 time=3.61 ms
64 bytes from 10.0.0.2: icmp_seq=79 ttl=64 time=3.88 ms
64 bytes from 10.0.0.2: icmp_seq=80 ttl=64 time=3.36 ms
64 bytes from 10.0.0.2: icmp_seq=81 ttl=64 time=4.76 ms
64 bytes from 10.0.0.2: icmp_seq=82 ttl=64 time=3.56 ms
64 bytes from 10.0.0.2: icmp_seq=83 ttl=64 time=4.16 ms
64 bytes from 10.0.0.2: icmp_seq=84 ttl=64 time=4.05 ms
64 bytes from 10.0.0.2: icmp_seq=85 ttl=64 time=4.23 ms
64 bytes from 10.0.0.2: icmp_seq=86 ttl=64 time=4.32 ms
64 bytes from 10.0.0.2: icmp_seq=87 ttl=64 time=3.95 ms
64 bytes from 10.0.0.2: icmp_seq=88 ttl=64 time=4.21 ms
64 bytes from 10.0.0.2: icmp_seq=89 ttl=64 time=3.88 ms
64 bytes from 10.0.0.2: icmp_seq=90 ttl=64 time=4.02 ms
64 bytes from 10.0.0.2: icmp_seq=91 ttl=64 time=4.33 ms
64 bytes from 10.0.0.2: icmp_seq=92 ttl=64 time=3.87 ms
64 bytes from 10.0.0.2: icmp_seq=93 ttl=64 time=4.17 ms
64 bytes from 10.0.0.2: icmp_seq=94 ttl=64 time=4.47 ms
64 bytes from 10.0.0.2: icmp_seq=95 ttl=64 time=4.24 ms
64 bytes from 10.0.0.2: icmp_seq=96 ttl=64 time=4.71 ms
64 bytes from 10.0.0.2: icmp_seq=97 ttl=64 time=1.75 ms
64 bytes from 10.0.0.2: icmp_seq=98 ttl=64 time=4.21 ms
64 bytes from 10.0.0.2: icmp_seq=99 ttl=64 time=4.23 ms
64 bytes from 10.0.0.2: icmp_seq=100 ttl=64 time=4.29 ms

--- 10.0.0.2 ping statistics ---
100 packets transmitted, 100 received, 0% packet loss, time 99162ms
rtt min/avg/max/mdev = 1.653/4.095/4.805/0.468 ms
mininet> 

For h1 ping -c100 h8
mininet> h1 ping -c100 h8
PING 10.0.0.8 (10.0.0.8) 56(84) bytes of data.
64 bytes from 10.0.0.8: icmp_seq=1 ttl=64 time=16.5 ms
64 bytes from 10.0.0.8: icmp_seq=2 ttl=64 time=9.35 ms
64 bytes from 10.0.0.8: icmp_seq=3 ttl=64 time=11.2 ms
64 bytes from 10.0.0.8: icmp_seq=4 ttl=64 time=9.40 ms
64 bytes from 10.0.0.8: icmp_seq=5 ttl=64 time=18.2 ms
64 bytes from 10.0.0.8: icmp_seq=6 ttl=64 time=17.4 ms
64 bytes from 10.0.0.8: icmp_seq=7 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=8 ttl=64 time=17.5 ms
64 bytes from 10.0.0.8: icmp_seq=9 ttl=64 time=17.7 ms
64 bytes from 10.0.0.8: icmp_seq=10 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=11 ttl=64 time=18.1 ms
64 bytes from 10.0.0.8: icmp_seq=12 ttl=64 time=17.8 ms
64 bytes from 10.0.0.8: icmp_seq=13 ttl=64 time=17.7 ms
64 bytes from 10.0.0.8: icmp_seq=14 ttl=64 time=17.7 ms
64 bytes from 10.0.0.8: icmp_seq=15 ttl=64 time=13.1 ms
64 bytes from 10.0.0.8: icmp_seq=16 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=17 ttl=64 time=18.1 ms
64 bytes from 10.0.0.8: icmp_seq=18 ttl=64 time=18.2 ms
64 bytes from 10.0.0.8: icmp_seq=19 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=20 ttl=64 time=17.5 ms
64 bytes from 10.0.0.8: icmp_seq=21 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=22 ttl=64 time=17.8 ms
64 bytes from 10.0.0.8: icmp_seq=23 ttl=64 time=17.7 ms
64 bytes from 10.0.0.8: icmp_seq=24 ttl=64 time=18.1 ms
64 bytes from 10.0.0.8: icmp_seq=25 ttl=64 time=17.7 ms
64 bytes from 10.0.0.8: icmp_seq=26 ttl=64 time=18.6 ms
64 bytes from 10.0.0.8: icmp_seq=27 ttl=64 time=18.0 ms
64 bytes from 10.0.0.8: icmp_seq=28 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=29 ttl=64 time=18.5 ms
64 bytes from 10.0.0.8: icmp_seq=30 ttl=64 time=18.1 ms
64 bytes from 10.0.0.8: icmp_seq=31 ttl=64 time=19.1 ms
64 bytes from 10.0.0.8: icmp_seq=32 ttl=64 time=18.5 ms
64 bytes from 10.0.0.8: icmp_seq=33 ttl=64 time=17.5 ms
64 bytes from 10.0.0.8: icmp_seq=34 ttl=64 time=17.5 ms
64 bytes from 10.0.0.8: icmp_seq=35 ttl=64 time=17.7 ms
64 bytes from 10.0.0.8: icmp_seq=36 ttl=64 time=17.6 ms
64 bytes from 10.0.0.8: icmp_seq=37 ttl=64 time=16.8 ms
64 bytes from 10.0.0.8: icmp_seq=38 ttl=64 time=17.9 ms
64 bytes from 10.0.0.8: icmp_seq=39 ttl=64 time=18.1 ms
64 bytes from 10.0.0.8: icmp_seq=40 ttl=64 time=17.5 ms
64 bytes from 10.0.0.8: icmp_seq=41 ttl=64 time=18.4 ms
64 bytes from 10.0.0.8: icmp_seq=42 ttl=64 time=17.3 ms
64 bytes from 10.0.0.8: icmp_seq=43 ttl=64 time=17.6 ms
64 bytes from 10.0.0.8: icmp_seq=44 ttl=64 time=18.1 ms
64 bytes from 10.0.0.8: icmp_seq=45 ttl=64 time=18.2 ms
64 bytes from 10.0.0.8: icmp_seq=46 ttl=64 time=17.7 ms
64 bytes from 10.0.0.8: icmp_seq=47 ttl=64 time=18.0 ms
64 bytes from 10.0.0.8: icmp_seq=48 ttl=64 time=18.1 ms
64 bytes from 10.0.0.8: icmp_seq=49 ttl=64 time=17.3 ms
64 bytes from 10.0.0.8: icmp_seq=50 ttl=64 time=18.2 ms
64 bytes from 10.0.0.8: icmp_seq=51 ttl=64 time=18.4 ms
64 bytes from 10.0.0.8: icmp_seq=52 ttl=64 time=14.5 ms
64 bytes from 10.0.0.8: icmp_seq=53 ttl=64 time=10.5 ms
64 bytes from 10.0.0.8: icmp_seq=54 ttl=64 time=17.5 ms
64 bytes from 10.0.0.8: icmp_seq=55 ttl=64 time=17.9 ms
64 bytes from 10.0.0.8: icmp_seq=56 ttl=64 time=17.5 ms
64 bytes from 10.0.0.8: icmp_seq=57 ttl=64 time=17.7 ms
64 bytes from 10.0.0.8: icmp_seq=58 ttl=64 time=17.2 ms
64 bytes from 10.0.0.8: icmp_seq=59 ttl=64 time=18.1 ms
64 bytes from 10.0.0.8: icmp_seq=60 ttl=64 time=17.9 ms
64 bytes from 10.0.0.8: icmp_seq=61 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=62 ttl=64 time=17.6 ms
64 bytes from 10.0.0.8: icmp_seq=63 ttl=64 time=18.0 ms
64 bytes from 10.0.0.8: icmp_seq=64 ttl=64 time=18.0 ms
64 bytes from 10.0.0.8: icmp_seq=65 ttl=64 time=17.6 ms
64 bytes from 10.0.0.8: icmp_seq=66 ttl=64 time=18.1 ms
64 bytes from 10.0.0.8: icmp_seq=67 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=68 ttl=64 time=5.60 ms
64 bytes from 10.0.0.8: icmp_seq=69 ttl=64 time=9.28 ms
64 bytes from 10.0.0.8: icmp_seq=70 ttl=64 time=9.34 ms
64 bytes from 10.0.0.8: icmp_seq=71 ttl=64 time=18.0 ms
64 bytes from 10.0.0.8: icmp_seq=72 ttl=64 time=9.06 ms
64 bytes from 10.0.0.8: icmp_seq=73 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=74 ttl=64 time=10.0 ms
64 bytes from 10.0.0.8: icmp_seq=75 ttl=64 time=5.21 ms
64 bytes from 10.0.0.8: icmp_seq=76 ttl=64 time=17.9 ms
64 bytes from 10.0.0.8: icmp_seq=77 ttl=64 time=18.0 ms
64 bytes from 10.0.0.8: icmp_seq=78 ttl=64 time=18.1 ms
64 bytes from 10.0.0.8: icmp_seq=79 ttl=64 time=18.1 ms
64 bytes from 10.0.0.8: icmp_seq=80 ttl=64 time=18.4 ms
64 bytes from 10.0.0.8: icmp_seq=81 ttl=64 time=18.1 ms
64 bytes from 10.0.0.8: icmp_seq=82 ttl=64 time=18.2 ms
64 bytes from 10.0.0.8: icmp_seq=83 ttl=64 time=8.88 ms
64 bytes from 10.0.0.8: icmp_seq=84 ttl=64 time=17.8 ms
64 bytes from 10.0.0.8: icmp_seq=85 ttl=64 time=17.6 ms
64 bytes from 10.0.0.8: icmp_seq=86 ttl=64 time=18.7 ms
64 bytes from 10.0.0.8: icmp_seq=87 ttl=64 time=18.0 ms
64 bytes from 10.0.0.8: icmp_seq=88 ttl=64 time=18.2 ms
64 bytes from 10.0.0.8: icmp_seq=89 ttl=64 time=18.7 ms
64 bytes from 10.0.0.8: icmp_seq=90 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=91 ttl=64 time=10.0 ms
64 bytes from 10.0.0.8: icmp_seq=92 ttl=64 time=9.92 ms
64 bytes from 10.0.0.8: icmp_seq=93 ttl=64 time=9.82 ms
64 bytes from 10.0.0.8: icmp_seq=94 ttl=64 time=10.2 ms
64 bytes from 10.0.0.8: icmp_seq=95 ttl=64 time=10.0 ms
64 bytes from 10.0.0.8: icmp_seq=96 ttl=64 time=11.2 ms
64 bytes from 10.0.0.8: icmp_seq=97 ttl=64 time=9.79 ms
64 bytes from 10.0.0.8: icmp_seq=98 ttl=64 time=9.42 ms
64 bytes from 10.0.0.8: icmp_seq=99 ttl=64 time=10.3 ms
64 bytes from 10.0.0.8: icmp_seq=100 ttl=64 time=12.2 ms

--- 10.0.0.8 ping statistics ---
100 packets transmitted, 100 received, 0% packet loss, time 99170ms
rtt min/avg/max/mdev = 5.216/16.149/19.155/3.537 ms
mininet> 
mininet> 

a. How long does it take (on average) to ping for each case?
ANS - 
h1 ping -c100 h2 -> 16.149 ms
h1 ping -c100 h8 -> 4.095 ms

b. What is the minimum and maximum ping you have observed?
ANS - 
Mininmum Ping
h1 ping -c100 h2 -> 1.653 ms
h1 ping -c100 h8 -> 5.216 ms

Maxinmum Ping
h1 ping -c100 h2 -> 5.216 ms
h1 ping -c100 h8 -> 19.155 ms

c. What is the difference, and why?
ANS - 
Between h1 and h8, ping times (the length of time it takes to send and receive a data packet)
are much longer than they are between h1 and h2. This is due to the fact that 
just one switch (s3) is present on the route between h1 and h2, although several 
switches are present on the route between h1 and h8 (s3, s2, s1, s5, s7).

3. Run “iperf h1 h2” and “iperf h1 h8”
ANS - 
mininet> 
mininet> iperf h1 h2
*** Iperf: testing TCP bandwidth between h1 and h2 
*** Results: ['7.36 Mbits/sec', '7.84 Mbits/sec']
mininet> iperf h1 h8
*** Iperf: testing TCP bandwidth between h1 and h8 
*** Results: ['2.50 Mbits/sec', '2.85 Mbits/sec']
mininet> 
mininet> 

a. What is “iperf” used for?
ANS - 

By measuring the bandwidth between two hosts, the free program Iperf enables network
managers to assess the effectiveness and quality of a network connection. 
The maximum amount of data that can be carried across the network link is determined
in part by this measurement. Iperf essentially enables the testing of the data throughput
between any two network nodes.

b. What is the throughput for each case?
ANS - 
*** Iperf: testing TCP bandwidth between h1 and h2 
*** Results: ['7.36 Mbits/sec', '7.84 Mbits/sec']
mininet> iperf h1 h8
*** Iperf: testing TCP bandwidth between h1 and h8 
*** Results: ['2.50 Mbits/sec', '2.85 Mbits/sec']

c. What is the difference, and explain the reasons for the difference?
ANS - 
Due to network congestion and latency, which also influences ping time, the data transfer
rate between h1 and h2 is faster than h1 and h8. More data may be sent more quickly
since there are fewer intermediate stops due to the shorter distance between h1 and h2.
The quantity of data that can be transmitted in a given period is reduced due to the
longer distance between h1 and h8, which requires more intermediate breaks.

4. Which of the switches observe traffic? Please describe your way for observing such
traffic on switches (e.g., adding some functions in the “of_tutorial” controller ?

ANS - 
We can inspect the information that aids in traffic observation by adding log.info("Switch observing traffic:%s"% (self.connection) to the line 107 "of tutorial" controller.
We can infer from it that all switches view the traffic, particularly when they are
all inundated with packets. The event listener, _handle PacketIn, is invoked each 
time a packet is received.

TASK - 3 

1. Describe how the above code works, such as how the "MAC to Port" map is established.
You could use a ‘ping’ example to describe the establishment process (e.g., h1 ping h2).
ANS - 
The switch function, known as "act like switch", has the ability to learn the locations of MAC addresses, enabling the controller to easily map
a MAC address to a port if it is a commonly used address. This helps improve the controller's efficiency in delivering packets to known addresses 
by directing them to the appropriate port. If the destination address is unknown, the function sends the packet to every destination. 
By reducing the frequency of packet flooding, the MAC Learning Controller also helps improve ping times and throughputs.

2. (Comment out all prints before doing this experiment) Have h1 ping h2, and h1 ping
h8 for 100 times (e.g., h1 ping -c100 p2).
ANS - 
mininet> h1 ping -c100 h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=4.42 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=4.31 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=4.55 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=1.76 ms
64 bytes from 10.0.0.2: icmp_seq=5 ttl=64 time=4.51 ms
64 bytes from 10.0.0.2: icmp_seq=6 ttl=64 time=4.00 ms
64 bytes from 10.0.0.2: icmp_seq=7 ttl=64 time=3.91 ms
64 bytes from 10.0.0.2: icmp_seq=8 ttl=64 time=4.23 ms
64 bytes from 10.0.0.2: icmp_seq=9 ttl=64 time=4.16 ms
64 bytes from 10.0.0.2: icmp_seq=10 ttl=64 time=4.28 ms
64 bytes from 10.0.0.2: icmp_seq=11 ttl=64 time=4.59 ms
64 bytes from 10.0.0.2: icmp_seq=12 ttl=64 time=4.24 ms
64 bytes from 10.0.0.2: icmp_seq=13 ttl=64 time=4.22 ms
64 bytes from 10.0.0.2: icmp_seq=14 ttl=64 time=4.24 ms
64 bytes from 10.0.0.2: icmp_seq=15 ttl=64 time=4.32 ms
64 bytes from 10.0.0.2: icmp_seq=16 ttl=64 time=4.19 ms
64 bytes from 10.0.0.2: icmp_seq=17 ttl=64 time=3.90 ms
64 bytes from 10.0.0.2: icmp_seq=18 ttl=64 time=4.23 ms
64 bytes from 10.0.0.2: icmp_seq=19 ttl=64 time=4.26 ms
64 bytes from 10.0.0.2: icmp_seq=20 ttl=64 time=4.22 ms
64 bytes from 10.0.0.2: icmp_seq=21 ttl=64 time=4.31 ms
64 bytes from 10.0.0.2: icmp_seq=22 ttl=64 time=3.92 ms
64 bytes from 10.0.0.2: icmp_seq=23 ttl=64 time=4.29 ms
64 bytes from 10.0.0.2: icmp_seq=24 ttl=64 time=4.78 ms
64 bytes from 10.0.0.2: icmp_seq=25 ttl=64 time=4.77 ms
64 bytes from 10.0.0.2: icmp_seq=26 ttl=64 time=3.56 ms
64 bytes from 10.0.0.2: icmp_seq=27 ttl=64 time=1.88 ms
64 bytes from 10.0.0.2: icmp_seq=28 ttl=64 time=5.16 ms
64 bytes from 10.0.0.2: icmp_seq=29 ttl=64 time=4.22 ms
64 bytes from 10.0.0.2: icmp_seq=30 ttl=64 time=4.38 ms
64 bytes from 10.0.0.2: icmp_seq=31 ttl=64 time=4.22 ms
64 bytes from 10.0.0.2: icmp_seq=32 ttl=64 time=4.66 ms
64 bytes from 10.0.0.2: icmp_seq=33 ttl=64 time=4.30 ms
64 bytes from 10.0.0.2: icmp_seq=34 ttl=64 time=4.24 ms
64 bytes from 10.0.0.2: icmp_seq=35 ttl=64 time=4.38 ms
64 bytes from 10.0.0.2: icmp_seq=36 ttl=64 time=3.54 ms
64 bytes from 10.0.0.2: icmp_seq=37 ttl=64 time=4.40 ms
64 bytes from 10.0.0.2: icmp_seq=38 ttl=64 time=4.23 ms
64 bytes from 10.0.0.2: icmp_seq=39 ttl=64 time=4.26 ms
64 bytes from 10.0.0.2: icmp_seq=40 ttl=64 time=4.35 ms
64 bytes from 10.0.0.2: icmp_seq=41 ttl=64 time=4.21 ms
64 bytes from 10.0.0.2: icmp_seq=42 ttl=64 time=3.57 ms
64 bytes from 10.0.0.2: icmp_seq=43 ttl=64 time=3.52 ms
64 bytes from 10.0.0.2: icmp_seq=44 ttl=64 time=3.55 ms
64 bytes from 10.0.0.2: icmp_seq=45 ttl=64 time=4.32 ms
64 bytes from 10.0.0.2: icmp_seq=46 ttl=64 time=4.32 ms
64 bytes from 10.0.0.2: icmp_seq=47 ttl=64 time=4.27 ms
64 bytes from 10.0.0.2: icmp_seq=48 ttl=64 time=3.94 ms
64 bytes from 10.0.0.2: icmp_seq=49 ttl=64 time=4.26 ms
64 bytes from 10.0.0.2: icmp_seq=50 ttl=64 time=4.42 ms
64 bytes from 10.0.0.2: icmp_seq=51 ttl=64 time=4.28 ms
64 bytes from 10.0.0.2: icmp_seq=52 ttl=64 time=4.21 ms
64 bytes from 10.0.0.2: icmp_seq=53 ttl=64 time=4.23 ms
64 bytes from 10.0.0.2: icmp_seq=54 ttl=64 time=4.29 ms
64 bytes from 10.0.0.2: icmp_seq=55 ttl=64 time=4.06 ms
64 bytes from 10.0.0.2: icmp_seq=56 ttl=64 time=4.28 ms
64 bytes from 10.0.0.2: icmp_seq=57 ttl=64 time=4.19 ms
64 bytes from 10.0.0.2: icmp_seq=58 ttl=64 time=4.25 ms
64 bytes from 10.0.0.2: icmp_seq=59 ttl=64 time=4.23 ms
64 bytes from 10.0.0.2: icmp_seq=60 ttl=64 time=4.33 ms
64 bytes from 10.0.0.2: icmp_seq=61 ttl=64 time=4.33 ms
64 bytes from 10.0.0.2: icmp_seq=62 ttl=64 time=4.26 ms
64 bytes from 10.0.0.2: icmp_seq=63 ttl=64 time=4.26 ms
64 bytes from 10.0.0.2: icmp_seq=64 ttl=64 time=4.34 ms
64 bytes from 10.0.0.2: icmp_seq=65 ttl=64 time=4.36 ms
64 bytes from 10.0.0.2: icmp_seq=66 ttl=64 time=4.25 ms
64 bytes from 10.0.0.2: icmp_seq=67 ttl=64 time=1.82 ms
64 bytes from 10.0.0.2: icmp_seq=68 ttl=64 time=4.30 ms
64 bytes from 10.0.0.2: icmp_seq=69 ttl=64 time=4.22 ms
64 bytes from 10.0.0.2: icmp_seq=70 ttl=64 time=4.28 ms
64 bytes from 10.0.0.2: icmp_seq=71 ttl=64 time=4.32 ms
64 bytes from 10.0.0.2: icmp_seq=72 ttl=64 time=4.20 ms
64 bytes from 10.0.0.2: icmp_seq=73 ttl=64 time=4.25 ms
64 bytes from 10.0.0.2: icmp_seq=74 ttl=64 time=4.29 ms
64 bytes from 10.0.0.2: icmp_seq=75 ttl=64 time=4.42 ms
64 bytes from 10.0.0.2: icmp_seq=76 ttl=64 time=4.63 ms
64 bytes from 10.0.0.2: icmp_seq=77 ttl=64 time=4.26 ms
64 bytes from 10.0.0.2: icmp_seq=78 ttl=64 time=3.53 ms
64 bytes from 10.0.0.2: icmp_seq=79 ttl=64 time=4.18 ms
64 bytes from 10.0.0.2: icmp_seq=80 ttl=64 time=4.31 ms
64 bytes from 10.0.0.2: icmp_seq=81 ttl=64 time=4.15 ms
64 bytes from 10.0.0.2: icmp_seq=82 ttl=64 time=3.93 ms
64 bytes from 10.0.0.2: icmp_seq=83 ttl=64 time=1.54 ms
64 bytes from 10.0.0.2: icmp_seq=84 ttl=64 time=4.26 ms
64 bytes from 10.0.0.2: icmp_seq=85 ttl=64 time=4.32 ms
64 bytes from 10.0.0.2: icmp_seq=86 ttl=64 time=4.05 ms
64 bytes from 10.0.0.2: icmp_seq=87 ttl=64 time=4.26 ms
64 bytes from 10.0.0.2: icmp_seq=88 ttl=64 time=4.21 ms
64 bytes from 10.0.0.2: icmp_seq=89 ttl=64 time=4.24 ms
64 bytes from 10.0.0.2: icmp_seq=90 ttl=64 time=4.41 ms
64 bytes from 10.0.0.2: icmp_seq=91 ttl=64 time=4.25 ms
64 bytes from 10.0.0.2: icmp_seq=92 ttl=64 time=4.19 ms
64 bytes from 10.0.0.2: icmp_seq=93 ttl=64 time=4.34 ms
64 bytes from 10.0.0.2: icmp_seq=94 ttl=64 time=4.23 ms
64 bytes from 10.0.0.2: icmp_seq=95 ttl=64 time=4.35 ms
64 bytes from 10.0.0.2: icmp_seq=96 ttl=64 time=4.19 ms
64 bytes from 10.0.0.2: icmp_seq=97 ttl=64 time=3.88 ms
64 bytes from 10.0.0.2: icmp_seq=98 ttl=64 time=2.19 ms
64 bytes from 10.0.0.2: icmp_seq=99 ttl=64 time=3.94 ms
64 bytes from 10.0.0.2: icmp_seq=100 ttl=64 time=4.33 ms

--- 10.0.0.2 ping statistics ---
100 packets transmitted, 100 received, 0% packet loss, time 99170ms
rtt min/avg/max/mdev = 1.544/4.116/5.161/0.581 ms

h1 ping -c00 h8
mininet> h1 ping -c100 h8
PING 10.0.0.8 (10.0.0.8) 56(84) bytes of data.
64 bytes from 10.0.0.8: icmp_seq=1 ttl=64 time=25.9 ms
64 bytes from 10.0.0.8: icmp_seq=2 ttl=64 time=17.2 ms
64 bytes from 10.0.0.8: icmp_seq=3 ttl=64 time=17.5 ms
64 bytes from 10.0.0.8: icmp_seq=4 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=5 ttl=64 time=13.3 ms
64 bytes from 10.0.0.8: icmp_seq=6 ttl=64 time=9.46 ms
64 bytes from 10.0.0.8: icmp_seq=7 ttl=64 time=10.1 ms
64 bytes from 10.0.0.8: icmp_seq=8 ttl=64 time=9.09 ms
64 bytes from 10.0.0.8: icmp_seq=9 ttl=64 time=17.8 ms
64 bytes from 10.0.0.8: icmp_seq=10 ttl=64 time=17.7 ms
64 bytes from 10.0.0.8: icmp_seq=11 ttl=64 time=16.9 ms
64 bytes from 10.0.0.8: icmp_seq=12 ttl=64 time=18.0 ms
64 bytes from 10.0.0.8: icmp_seq=13 ttl=64 time=16.8 ms
64 bytes from 10.0.0.8: icmp_seq=14 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=15 ttl=64 time=18.7 ms
64 bytes from 10.0.0.8: icmp_seq=16 ttl=64 time=17.6 ms
64 bytes from 10.0.0.8: icmp_seq=17 ttl=64 time=17.8 ms
64 bytes from 10.0.0.8: icmp_seq=18 ttl=64 time=17.4 ms
64 bytes from 10.0.0.8: icmp_seq=19 ttl=64 time=17.5 ms
64 bytes from 10.0.0.8: icmp_seq=20 ttl=64 time=12.6 ms
64 bytes from 10.0.0.8: icmp_seq=21 ttl=64 time=9.77 ms
64 bytes from 10.0.0.8: icmp_seq=22 ttl=64 time=10.3 ms
64 bytes from 10.0.0.8: icmp_seq=23 ttl=64 time=9.93 ms
64 bytes from 10.0.0.8: icmp_seq=24 ttl=64 time=9.98 ms
64 bytes from 10.0.0.8: icmp_seq=25 ttl=64 time=13.0 ms
64 bytes from 10.0.0.8: icmp_seq=26 ttl=64 time=17.7 ms
64 bytes from 10.0.0.8: icmp_seq=27 ttl=64 time=16.4 ms
64 bytes from 10.0.0.8: icmp_seq=28 ttl=64 time=17.3 ms
64 bytes from 10.0.0.8: icmp_seq=29 ttl=64 time=16.1 ms
64 bytes from 10.0.0.8: icmp_seq=30 ttl=64 time=16.8 ms
64 bytes from 10.0.0.8: icmp_seq=31 ttl=64 time=16.8 ms
64 bytes from 10.0.0.8: icmp_seq=32 ttl=64 time=17.5 ms
64 bytes from 10.0.0.8: icmp_seq=33 ttl=64 time=18.7 ms
64 bytes from 10.0.0.8: icmp_seq=34 ttl=64 time=16.6 ms
64 bytes from 10.0.0.8: icmp_seq=35 ttl=64 time=16.6 ms
64 bytes from 10.0.0.8: icmp_seq=36 ttl=64 time=17.2 ms
64 bytes from 10.0.0.8: icmp_seq=37 ttl=64 time=16.1 ms
64 bytes from 10.0.0.8: icmp_seq=38 ttl=64 time=16.3 ms
64 bytes from 10.0.0.8: icmp_seq=39 ttl=64 time=17.1 ms
64 bytes from 10.0.0.8: icmp_seq=40 ttl=64 time=16.4 ms
64 bytes from 10.0.0.8: icmp_seq=41 ttl=64 time=14.9 ms
64 bytes from 10.0.0.8: icmp_seq=42 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=43 ttl=64 time=16.2 ms
64 bytes from 10.0.0.8: icmp_seq=44 ttl=64 time=16.8 ms
64 bytes from 10.0.0.8: icmp_seq=45 ttl=64 time=16.8 ms
64 bytes from 10.0.0.8: icmp_seq=46 ttl=64 time=16.0 ms
64 bytes from 10.0.0.8: icmp_seq=47 ttl=64 time=15.6 ms
64 bytes from 10.0.0.8: icmp_seq=48 ttl=64 time=16.3 ms
64 bytes from 10.0.0.8: icmp_seq=49 ttl=64 time=16.8 ms
64 bytes from 10.0.0.8: icmp_seq=50 ttl=64 time=16.6 ms
64 bytes from 10.0.0.8: icmp_seq=51 ttl=64 time=17.4 ms
64 bytes from 10.0.0.8: icmp_seq=52 ttl=64 time=16.6 ms
64 bytes from 10.0.0.8: icmp_seq=53 ttl=64 time=16.0 ms
64 bytes from 10.0.0.8: icmp_seq=54 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=55 ttl=64 time=16.8 ms
64 bytes from 10.0.0.8: icmp_seq=56 ttl=64 time=17.4 ms
64 bytes from 10.0.0.8: icmp_seq=57 ttl=64 time=16.1 ms
64 bytes from 10.0.0.8: icmp_seq=58 ttl=64 time=17.3 ms
64 bytes from 10.0.0.8: icmp_seq=59 ttl=64 time=17.4 ms
64 bytes from 10.0.0.8: icmp_seq=60 ttl=64 time=16.1 ms
64 bytes from 10.0.0.8: icmp_seq=61 ttl=64 time=17.5 ms
64 bytes from 10.0.0.8: icmp_seq=62 ttl=64 time=16.2 ms
64 bytes from 10.0.0.8: icmp_seq=63 ttl=64 time=16.9 ms
64 bytes from 10.0.0.8: icmp_seq=64 ttl=64 time=15.8 ms
64 bytes from 10.0.0.8: icmp_seq=65 ttl=64 time=16.9 ms
64 bytes from 10.0.0.8: icmp_seq=66 ttl=64 time=17.4 ms
64 bytes from 10.0.0.8: icmp_seq=67 ttl=64 time=15.6 ms
64 bytes from 10.0.0.8: icmp_seq=68 ttl=64 time=17.4 ms
64 bytes from 10.0.0.8: icmp_seq=69 ttl=64 time=16.2 ms
64 bytes from 10.0.0.8: icmp_seq=70 ttl=64 time=16.2 ms
64 bytes from 10.0.0.8: icmp_seq=71 ttl=64 time=17.4 ms
64 bytes from 10.0.0.8: icmp_seq=72 ttl=64 time=16.6 ms
64 bytes from 10.0.0.8: icmp_seq=73 ttl=64 time=16.3 ms
64 bytes from 10.0.0.8: icmp_seq=74 ttl=64 time=18.0 ms
64 bytes from 10.0.0.8: icmp_seq=75 ttl=64 time=16.5 ms
64 bytes from 10.0.0.8: icmp_seq=76 ttl=64 time=16.7 ms
64 bytes from 10.0.0.8: icmp_seq=77 ttl=64 time=16.8 ms
64 bytes from 10.0.0.8: icmp_seq=78 ttl=64 time=17.1 ms
64 bytes from 10.0.0.8: icmp_seq=79 ttl=64 time=17.2 ms
64 bytes from 10.0.0.8: icmp_seq=80 ttl=64 time=16.3 ms
64 bytes from 10.0.0.8: icmp_seq=81 ttl=64 time=17.1 ms
64 bytes from 10.0.0.8: icmp_seq=82 ttl=64 time=18.3 ms
64 bytes from 10.0.0.8: icmp_seq=83 ttl=64 time=17.4 ms
64 bytes from 10.0.0.8: icmp_seq=84 ttl=64 time=17.5 ms
64 bytes from 10.0.0.8: icmp_seq=85 ttl=64 time=16.0 ms
64 bytes from 10.0.0.8: icmp_seq=86 ttl=64 time=16.6 ms
64 bytes from 10.0.0.8: icmp_seq=87 ttl=64 time=16.7 ms
64 bytes from 10.0.0.8: icmp_seq=88 ttl=64 time=16.7 ms
64 bytes from 10.0.0.8: icmp_seq=89 ttl=64 time=16.4 ms
64 bytes from 10.0.0.8: icmp_seq=90 ttl=64 time=17.5 ms
64 bytes from 10.0.0.8: icmp_seq=91 ttl=64 time=17.3 ms
64 bytes from 10.0.0.8: icmp_seq=92 ttl=64 time=16.5 ms
64 bytes from 10.0.0.8: icmp_seq=93 ttl=64 time=17.0 ms
64 bytes from 10.0.0.8: icmp_seq=94 ttl=64 time=17.5 ms
64 bytes from 10.0.0.8: icmp_seq=95 ttl=64 time=17.1 ms
64 bytes from 10.0.0.8: icmp_seq=96 ttl=64 time=17.3 ms
64 bytes from 10.0.0.8: icmp_seq=97 ttl=64 time=16.4 ms
64 bytes from 10.0.0.8: icmp_seq=98 ttl=64 time=9.68 ms
64 bytes from 10.0.0.8: icmp_seq=99 ttl=64 time=9.82 ms
64 bytes from 10.0.0.8: icmp_seq=100 ttl=64 time=17.7 ms

--- 10.0.0.8 ping statistics ---
100 packets transmitted, 100 received, 0% packet loss, time 99175ms
rtt min/avg/max/mdev = 9.095/16.341/25.928/2.445 ms

a. How long did it take (on average) to ping for each case?
ANS - 
h1 ping -c100 h2 4.116 ms
h1 ping -c100 h8 16.341 ms

b. What is the minimum and maximum ping you have observed?
ANS - 
Mininmum Ping
h1 ping -c100 h2 -> 1.544
h1 ping -c100 h8 -> 9.095

Maxinmum Ping
h1 ping -c100 h2 -> 5.161
h1 ping -c100 h8 -> 25.928

c. Any difference from Task 2 and why do you think there is a change if there is?
ANS - 
Although the difference is not that great, task 3's value for h1 ping h2 takes slightly 
less time than task 2's. However, because there are many more switches to pass through 
in the case of h1 and h8, the difference is considerable for ping time numbers. 
When only the first few packets are flooded in job 3, it is obvious that task 3 is substantially 
faster or has a lower ping time. The switches will only resend the packet to the "mac to port" 
mapping's associated port after locating the destination MAC address in the map. However, because there won't be as much network congestion,the following pings are significantly faster.

3. Q.3 Run “iperf h1 h2” and “iperf h1 h8”.
a. What is the throughput for each case?
b. What is the difference from Task 2 and why do you think there is a change if
there is?
