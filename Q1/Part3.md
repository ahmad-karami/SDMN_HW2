# when the namespaces are on different servers that can see each other in layer 2
in this case when servers can see each other in layer 2 it means that they are in the same network.

# explain
in this scenario like the previous one we need to have two virtual interfaces, that connect the root namespace of the server to the node namespace and each interface that connect to the root namespace should have an ip address that is the defualt gateway of it's network nodes. and the ip forwarding of the root namespace should be enable in each server.

here the middle layer2 switch should be able to handel arp packets.

## key feature
the important feature that that we should use here is NAT beacuse our nodes namespaces network are different from the servers network so kernel should work as a NAT and route the data to the dest server and the dest server translate the data for the nodes namespace.