import subprocess
import sys
import os

hostname = sys.argv[1]
# print(hostname)

# subprocess.run(['unshare', '-n', '-u', '-i', '-p', '-f', '-m', '-U'])

# subprocess.run(['mount', '--make-rprivate', '/'])
# subprocess.run(['mount', '-t', 'tmpfs', 'none', '/tmp'])
# subprocess.run(['mount', '-t', 'proc', 'none', '/proc'])

# os.chdir('/tmp')
# os.mkdir('rootfs')
# subprocess.run(['debootstrap', '--variant=minbase', '--arch=amd64', 'stretch', './rootfs'])
# os.chdir('./rootfs')
# subprocess.run(['mount', '-t', 'proc', 'none', '/proc'])
# subprocess.run(['mount', '-t', 'sysfs', 'none', '/sys'])
    
# subprocess.run(['hostnamectl', 'set-hostname', hostname])    

def Root_Dir(hostname):
    # make root directories  
    subprocess.run(['mkdir',f'./{hostname}']) 
    subprocess.run(['mkdir',f'./{hostname}/bin']) 
    subprocess.run(['mkdir',f'./{hostname}/lib64']) 
    subprocess.run(['mkdir',f'./{hostname}/lib'])

    # copy bash and ls  and ip exec files
    subprocess.run(['cp' ,'/bin/bash', f'{hostname}/bin'])
    subprocess.run(['cp' ,'/bin/ls', f'{hostname}/bin'])
    subprocess.run(['cp' ,'/bin/ip', f'{hostname}/bin'])

    subprocess.run(['cp' ,'/bin/hostnamectl', f'{hostname}/bin'])
    subprocess.run(['cp' ,'/bin/ps', f'{hostname}/bin'])

    # copy libraries needed for bash and ls
    subprocess.run(['cp','/lib/x86_64-linux-gnu/libpcre2-8.so.0','/lib/x86_64-linux-gnu/libc.so.6','/lib/x86_64-linux-gnu/libselinux.so.1','/lib/x86_64-linux-gnu/libtinfo.so.6', f'{hostname}/lib'])
    subprocess.run(['cp','/lib64/ld-linux-x86-64.so.2', f'{hostname}/lib64'])
    
    # copy libraries needed for ip
    subprocess.run(['cp','/lib/x86_64-linux-gnu/libbpf.so.0','/lib/x86_64-linux-gnu/libelf.so.1','/lib/x86_64-linux-gnu/libmnl.so.0','/lib/x86_64-linux-gnu/libbsd.so.0', f'{hostname}/lib'])
    subprocess.run(['cp','/lib/x86_64-linux-gnu/libcap.so.2','/lib/x86_64-linux-gnu/libz.so.1','/lib/x86_64-linux-gnu/libmd.so.0','/lib/x86_64-linux-gnu/libbsd.so.0', f'{hostname}/lib'])

    # copy libraries needed for hostnamectl
    subprocess.run(['cp','/lib/systemd/libsystemd-shared-249.so','/lib/x86_64-linux-gnu/libacl.so.1','/lib/x86_64-linux-gnu/libblkid.so.1','/lib/x86_64-linux-gnu/libcrypt.so.1','/lib/x86_64-linux-gnu/libgcrypt.so.20',f'{hostname}/lib'])
    subprocess.run(['cp','/lib/x86_64-linux-gnu/libip4tc.so.2','/lib/x86_64-linux-gnu/libkmod.so.2','/lib/x86_64-linux-gnu/liblz4.so.1','/lib/x86_64-linux-gnu/libmount.so.1',f'{hostname}/lib'])
    subprocess.run(['cp','/lib/x86_64-linux-gnu/libcrypto.so.3','/lib/x86_64-linux-gnu/libpam.so.0','/lib/x86_64-linux-gnu/libseccomp.so.2','/lib/x86_64-linux-gnu/libzstd.so.1',f'{hostname}/lib'])
    subprocess.run(['cp','/lib/x86_64-linux-gnu/liblzma.so.5','/lib/x86_64-linux-gnu/libgpg-error.so.0','/lib/x86_64-linux-gnu/libaudit.so.1','/lib/x86_64-linux-gnu/libcap-ng.so.0',f'{hostname}/lib'])
    
    subprocess.run(['cp','/lib/x86_64-linux-gnu/libprocps.so.8','/lib/x86_64-linux-gnu/libsystemd.so.0',f'{hostname}/lib'])
    

    subprocess.run(['chroot' ,f'{hostname}'])

# Root_Dir(hostname)

def create_namespaces():
    subprocess.run(['unshare', '--pid' ,'--net','--uts', '--map-root-user','--mount-proc','--fork','bash'])



# create_namespaces()
Root_Dir(hostname)



#subprocess.run(['hostnamectl', 'set-hostname', hostname])


















# prosses

# chroot

# bash
