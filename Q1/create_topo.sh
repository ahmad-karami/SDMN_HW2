# create topology
# build net namespace
ip netns add ns1	
ip netns add ns2
ip netns add ns3	
ip netns add ns4
ip netns add router

# create bridges 
ip link add br1 type bridge
ip link add br2 type bridge
ip link set dev br1 up
ip link set dev br2 up

# create veth pairs
ip link add veth_ns1 type veth peer name veth_ns1_br1
ip link add veth_ns2 type veth peer name veth_ns2_br1
ip link add veth_ns3 type veth peer name veth_ns3_br2
ip link add veth_ns4 type veth peer name veth_ns4_br2

ip link add veth_nsr_br1 type veth peer name veth_rbr1
ip link add veth_nsr_br2 type veth peer name veth_rbr2

# attach each interface to corresponding namespace 
ip link set veth_ns1 netns ns1
ip link set veth_ns2 netns ns2
ip link set veth_ns3 netns ns3
ip link set veth_ns4 netns ns4

ip link set veth_rbr1 netns router
ip link set veth_rbr2 netns router

ip link set veth_ns1_br1 master br1
ip link set veth_ns2_br1 master br1
ip link set veth_nsr_br1 master br1

ip link set veth_ns3_br2 master br2
ip link set veth_ns4_br2 master br2
ip link set veth_nsr_br2 master br2

# Bring all intefacese up
ip netns exec ns1 ip link set veth_ns1 up
ip netns exec ns2 ip link set veth_ns2 up
ip netns exec ns3 ip link set veth_ns3 up
ip netns exec ns4 ip link set veth_ns4 up

ip netns exec router ip link set veth_rbr1 up
ip netns exec router ip link set veth_rbr2 up

ip link set veth_ns1_br1 up 
ip link set veth_ns2_br1 up 
ip link set veth_nsr_br1 up 

ip link set veth_ns3_br2 up 
ip link set veth_ns4_br2 up
ip link set veth_nsr_br2 up

# configure ip addr
ip netns exec ns1 ip addr add 172.0.0.2/24 dev veth_ns1
ip netns exec ns2 ip addr add 172.0.0.3/24 dev veth_ns2
ip netns exec ns3 ip addr add 10.10.0.2/24 dev veth_ns3
ip netns exec ns4 ip addr add 10.10.0.3/24 dev veth_ns4
ip netns exec router ip addr add 172.0.0.1/24 dev veth_rbr1
ip netns exec router ip addr add 10.10.0.1/24 dev veth_rbr2

# set routing rule
ip netns exec router sysctl -w net.ipv4.ip_forward=1

# set defualt gateway
ip netns exec ns1 ip route add default via 172.0.0.1
ip netns exec ns2 ip route add default via 172.0.0.1
ip netns exec ns3 ip route add default via 10.10.0.1
ip netns exec ns4 ip route add default via 10.10.0.1





