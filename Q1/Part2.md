# when we delete the router and it's links to the bridge
Without the router, we can use Linux IP forwarding in the root namespace to route packets between the two subnets connected to the two bridges.

# steps 
## step 1
First, we need to enable IP forwarding in the root namespace 

## step 2
Next, we need to create two new virtual interfaces in the root namespace, one for each subnet and move one end of each virtual interface pair to the corresponding subnet namespace

## step 3 
Then, we need to assign IP addresses to the virtual interfaces in the root namespace and finally assign 
default gateway for each node of the nework , the interface ip of the virtual interface in the root.


