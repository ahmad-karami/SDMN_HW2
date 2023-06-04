import subprocess
import sys
import os

hostname = sys.argv[1]
print(hostname)

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


subprocess.call(['mkdir','./jail']) 
subprocess.call(['mkdir','./jail/bin']) 
subprocess.call(['mkdir','./jail/lib64']) 
subprocess.call(['mkdir','./jail/lib']) 
# os.chdir('jail')
# print(os.getcwd())
subprocess.call(['cp' ,'/bin/bash', 'jail/bin'])
subprocess.call(['cp' ,'/bin/ls', 'jail/bin'])

# subprocess.call(['cp' ,'-v','/lib/x86_64-linux-gnu/libtinfo.so.6','jail/lib64'])
# subprocess.call(['cp' ,'-v','/lib/x86_64-linux-gnu/libc.so.6','jail/lib64'])

# subprocess.call(['cp' ,'-v','/lib/x86_64-linux-gnu/libselinux.so.1','jail/lib64'])
# subprocess.call(['cp' ,'-v','/lib/x86_64-linux-gnu/libc.so.6','jail/lib64'])
# subprocess.call(['cp' ,'-v','/lib/x86_64-linux-gnu/libpcre2-8.so.0','jail/lib64'])

subprocess.call(['cp','/lib/x86_64-linux-gnu/libpcre2-8.so.0','/lib/x86_64-linux-gnu/libc.so.6','/lib/x86_64-linux-gnu/libselinux.so.1','/lib/x86_64-linux-gnu/libtinfo.so.6', 'jail/lib'])
subprocess.call(['cp','/lib64/ld-linux-x86-64.so.2', 'jail/lib64'])

subprocess.call(['chroot' ,'jail'])
subprocess.call(['hostnamectl', 'set-hostname', hostname])


















# prosses

# chroot

# bash
