import subprocess
import os
import sys

# #text = input("prompt")
# #print(sys.argv)
# #print('badi')
# subprocess.call(['unshare', '-n', '-u', '-i', '-p', '-f', '-m', '-U'])

# print(hostname)
# subprocess.call(['mount', '--make-rprivate', '/'])
# subprocess.call(['mount', '-t', 'tmpfs', 'none', '/tmp'])
# subprocess.call(['mount', '-t', 'proc', 'none', '/proc'])

# os.chdir('/tmp')
# os.mkdir('rootfs')
# subprocess.call(['debootstrap', '--variant=minbase', '--arch=amd64', 'stretch', './rootfs'])
# os.chdir('./rootfs')
# subprocess.call(['mount', '-t', 'proc', 'none', '/proc'])
# subprocess.call(['mount', '-t', 'sysfs', 'none', '/sys'])
    
# subprocess.call(['hostnamectl', 'set-hostname', hostname])    
# def create_container(hostname):
#     # Create new namespaces for the container
#     subprocess.call(['unshare', '-n', '-u', '-i', '-p', '-f', '-m', '-U'])
    
#     # Mount a new file system for the container
#     subprocess.call(['mount', '--make-rprivate', '/'])
#     subprocess.call(['mount', '-t', 'tmpfs', 'none', '/tmp'])
#     subprocess.call(['mount', '-t', 'proc', 'none', '/proc'])
    
#     # Change the root directory of the container to the new file system
#     os.chdir('/tmp')
#     os.mkdir('rootfs')
#     subprocess.call(['rootfs', '--variant=minbase', '--arch=amd64', 'stretch', './rootfs'])
#     os.chdir('./rootfs')
#     subprocess.call(['mount', '-t', 'proc', 'none', '/proc'])
#     subprocess.call(['mount', '-t', 'sysfs', 'none', '/sys'])
    
#     # Set the hostname for the container
#     subprocess.call(['hostnamectl', 'set-hostname', hostname])
    
#     # Configure the network namespace for the container
#     # subprocess.call(['ip', 'link', 'set', 'lo', 'up'])
#     # subprocess.call(['ip', 'link', 'add', 'veth0', 'type', 'veth', 'peer', 'name', 'veth1'])
#     # subprocess.call(['ip', 'addr', 'add', '192.168.1.1/24', 'dev', 'veth0'])
#     # subprocess.call(['ip', 'link', 'set', 'veth0', 'up'])
#     # subprocess.call(['ip', 'link', 'set', 'veth1', 'netns', str(os.getpid())])
#     # subprocess.call(['ip', 'netns', 'exec', str(os.getpid()), 'ip', 'addr', 'add', '192.168.1.2/24', 'dev', 'veth1'])
#     # subprocess.call(['ip', 'netns', 'exec', str(os.getpid()), 'ip', 'link', 'set', 'veth1', 'up'])
#     # subprocess.call(['ip', 'netns', 'exec', str(os.getpid()), 'ip', 'route', 'add', 'default', 'via', '192.168.1.1'])
    

# def create_container(hostname):
#     # Create namespaces
#     subprocess.run(['ip', 'netns', 'add', hostname], check=True)
#     subprocess.run(['ip', 'netns', 'exec', hostname, 'ip', 'link', 'set', 'lo', 'up'], check=True)
#     subprocess.run(['ip', 'netns', 'exec', hostname, 'ip', 'link', 'set', 'eth0', 'up'], check=True)
#     subprocess.run(['ip', 'netns', 'exec', hostname, 'ip', 'addr', 'add', '127.0.0.1/8', 'dev', 'lo'], check=True)
#     subprocess.run(['ip', 'netns', 'exec', hostname, 'ip', 'addr', 'add', '192.168.0.2/24', 'dev', 'eth0'], check=True)

#     # Create mount namespace
#     subprocess.run(['unshare', '-m', 'bash'], check=True)

#     # Create PID namespace
#     subprocess.run(['unshare', '-p', 'bash'], check=True)

#     # Create UTS namespace
#     subprocess.run(['unshare', '-u', 'bash'], check=True)

#     # Start container
#     subprocess.run(['ip', 'netns', 'exec', hostname, 'bash'], check=True)

# Usage example
# import argparse
# def create_namespaces():
#     subprocess.run(['unshare', '--net'], check=True)
#     subprocess.run(['unshare', '--mount'], check=True)
#     subprocess.run(['unshare', '--pid'], check=True)
#     subprocess.run(['unshare', '--uts'], check=True)

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('hostname', help='Hostname for the container')
#     args = parser.parse_args()

# create_namespaces()
# create_container('mycontainer')  
# 
# 
# 
# Create namespaces
hostname = sys.argv[1]
print(hostname)
subprocess.run(['ip', 'netns', 'add', hostname], check=True)
# subprocess.run(['ip', 'netns', 'exec', hostname, 'ip', 'link', 'set', 'lo', 'up'], check=True)
#     subprocess.run(['ip', 'netns', 'exec', hostname, 'ip', 'link', 'set', 'eth0', 'up'], check=True)
#     subprocess.run(['ip', 'netns', 'exec', hostname, 'ip', 'addr', 'add', '127.0.0.1/8', 'dev', 'lo'], check=True)
#     subprocess.run(['ip', 'netns', 'exec', hostname, 'ip', 'addr', 'add', '192.168.0.2/24', 'dev', 'eth0'], check=True)

# Create mount namespace
subprocess.run(['unshare', '-m', 'bash'], check=True)

# Create PID namespace
subprocess.run(['unshare', '-p', 'bash'], check=True)

# Create UTS namespace
subprocess.run(['unshare', '-u', 'bash'], check=True)

# Start container
subprocess.run(['ip', 'netns', 'exec', hostname, 'bash'], check=True)
  

# create_container(hostname)
