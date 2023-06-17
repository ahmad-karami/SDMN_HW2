# Running code
my code is in golang and to run the file we use this command:
'''
go run Container.go <container_name> <memory_limit_in_MB>
'''
# Explain
this CLI command make a container with the <container_name> and set memory restraint to <memory_limit_in_MB>.

## namespace func
in my code first I define a namespace function that make all requiered namespaces and run another process that's name is "child function", inside it, that it's mean two parallel process are runinng.

## child func
in child function I define control group for my container then set host name for it and change the root filesystem that the container cansee just the root directory of the container after that I mount the proc directory to able my container to run exec files and then I use command to change CLI prumpt to the container name and after that I run a bash inside the container to use CLI.

## cgroup func
in cgroup function I make a directory for each of my containers and assign some control rules to them.

## file_sys & extractFile func
my code look for the ubuntu:20.04 file system in specific folder if it dosen't exeist it will download it and after that it will extract the downloaded file to the folder that is for the container.

## Ip func
run the ip addr command and show the output