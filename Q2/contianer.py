import subprocess
import sys
import os

hostname = sys.argv[1]
# print(hostname)

# subprocess.call(['unshare', '-n', '-u', '-i', '-p', '-f', '-m', '-U'])

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

def Root_Dir(hostname):
    # make root directories  
    subprocess.call(['mkdir',f'./{hostname}']) 
    subprocess.call(['mkdir',f'./{hostname}/bin']) 
    subprocess.call(['mkdir',f'./{hostname}/lib64']) 
    subprocess.call(['mkdir',f'./{hostname}/lib'])

    # copy bash and ls  and ip exec files
    subprocess.call(['cp' ,'/bin/bash', f'{hostname}/bin'])
    subprocess.call(['cp' ,'/bin/ls', f'{hostname}/bin'])
    subprocess.call(['cp' ,'/bin/ip', f'{hostname}/bin'])

    # copy libraries needed for bash and ls
    subprocess.call(['cp','/lib/x86_64-linux-gnu/libpcre2-8.so.0','/lib/x86_64-linux-gnu/libc.so.6','/lib/x86_64-linux-gnu/libselinux.so.1','/lib/x86_64-linux-gnu/libtinfo.so.6', f'{hostname}/lib'])
    subprocess.call(['cp','/lib64/ld-linux-x86-64.so.2', f'{hostname}/lib64'])
    
    # copy libraries needed for ip
    subprocess.call(['cp','/lib/x86_64-linux-gnu/libbpf.so.0','/lib/x86_64-linux-gnu/libelf.so.1','/lib/x86_64-linux-gnu/libmnl.so.0','/lib/x86_64-linux-gnu/libbsd.so.0', f'{hostname}/lib'])
    subprocess.call(['cp','/lib/x86_64-linux-gnu/libcap.so.2','/lib/x86_64-linux-gnu/libz.so.1','/lib/x86_64-linux-gnu/libmd.so.0','/lib/x86_64-linux-gnu/libbsd.so.0', f'{hostname}/lib'])

    subprocess.call(['chroot' ,f'{hostname}'])

# Root_Dir(hostname)

def create_namespaces():
    subprocess.run(['unshare', '--net'], check=True)
    subprocess.run(['unshare', '--mount'], check=True)
    subprocess.run(['unshare', '--pid'], check=True)
    subprocess.run(['unshare', '--uts'], check=True)

create_namespaces()
#subprocess.call(['hostnamectl', 'set-hostname', hostname])


















# prosses

# chroot

# bash
