package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"os/exec"
	"path/filepath"
	"strconv"
	"syscall"
)

func main() {
	switch os.Args[1] {
	case "child":
		child(os.Args[2], os.Args[3])
	default:
		Dir(os.Args[1])
		namespace(os.Args[1])
		// Container := os.Args[1]
	}
}

func namespace(Container string) {
	fmt.Printf("Running main %v as %d\n", os.Args[1:], os.Getpid())

	//define command
	cmd := exec.Command("/proc/self/exe", append([]string{"child"}, os.Args[1:]...)...)

	// set the standard input, output, and error streams of the command
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	// system-specific attributes for the process
	cmd.SysProcAttr = &syscall.SysProcAttr{
		Cloneflags: syscall.CLONE_NEWUTS | syscall.CLONE_NEWPID | syscall.CLONE_NEWNS | syscall.CLONE_NEWNET,
		// isolate namespaces
		Unshareflags: syscall.CLONE_NEWNS,
	}
	// Run the command
	cmd.Run()

}

func child(Container string, M_max string) {
	//for child founction i add an entity after main.go
	// Container := "container"
	fmt.Printf("Running child %v as %d\n", os.Args[1:], os.Getpid())

	Cgroup(M_max)
	// change the host name
	syscall.Sethostname([]byte(Container))

	syscall.Chroot(Container)
	syscall.Chdir("/")
	syscall.Mount("proc", "proc", "proc", 0, "")
	os.Setenv("PS1", "root@\\h:\\w$ ")
	//define command
	cmd := exec.Command("/bin/bash")
	// [1:child,2:/bin/bash,3:empty]

	// set the standard input, output, and error streams of the command
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	// Run the command
	cmd.Run()

	syscall.Unmount("/proc", 0)

}

func Cgroup(M_max string) {
	dir := "/sys/fs/cgroup/SDMN"
	os.Mkdir(dir, 0755)

	ioutil.WriteFile(filepath.Join(dir, "/pids.max"), []byte("20"), 0700)
	ioutil.WriteFile(filepath.Join(dir, "/memory.max"), []byte(M_max+"M"), 0700)
	ioutil.WriteFile(filepath.Join(dir, "/notify_on_release"), []byte("1"), 0700)
	ioutil.WriteFile(filepath.Join(dir, "/cgroup.procs"), []byte(strconv.Itoa(os.Getpid())), 0700)

}

func Dir(Container string) {

	// Container := "container"

	Bin := Container + "/bin"
	Lib := Container + "/lib"
	Lib64 := Container + "/lib64"
	Proc := Container + "/proc"
	Home := Container + "/home"
	// make directories
	os.Mkdir(Container, 0777)
	os.Mkdir(Bin, 0777)
	os.Mkdir(Lib, 0777)
	os.Mkdir(Lib64, 0777)
	os.Mkdir(Proc, 0777)
	os.Mkdir(Proc, 0777)
	os.Mkdir(Home, 0777)

	// exec files what we need in new root file system
	Copy("/bin/bash", Bin)
	Copy("/bin/ls", Bin)
	Copy("/bin/ip", Bin)
	Copy("/bin/ps", Bin)
	Copy("/bin/hostname", Bin)

	// library files for exec files
	Copy("/lib/x86_64-linux-gnu/libpcre2-8.so.0", Lib)
	Copy("/lib/x86_64-linux-gnu/libc.so.6", Lib)
	Copy("/lib/x86_64-linux-gnu/libselinux.so.1", Lib)
	Copy("/lib/x86_64-linux-gnu/libtinfo.so.6", Lib)
	Copy("/lib/x86_64-linux-gnu/libbpf.so.0", Lib)
	Copy("/lib/x86_64-linux-gnu/libelf.so.1", Lib)
	Copy("/lib/x86_64-linux-gnu/libmnl.so.0", Lib)
	Copy("/lib/x86_64-linux-gnu/libbsd.so.0", Lib)
	Copy("/lib/x86_64-linux-gnu/libcap.so.2", Lib)
	Copy("/lib/x86_64-linux-gnu/libz.so.1", Lib)
	Copy("/lib/x86_64-linux-gnu/libmd.so.0", Lib)
	Copy("/lib/x86_64-linux-gnu/libbsd.so.0", Lib)
	Copy("/lib/x86_64-linux-gnu/libprocps.so.8", Lib)
	Copy("/lib/x86_64-linux-gnu/liblzma.so.5", Lib)
	Copy("/lib/x86_64-linux-gnu/libzstd.so.1", Lib)
	Copy("/lib/x86_64-linux-gnu/liblz4.so.1", Lib)
	Copy("/lib/x86_64-linux-gnu/libgcrypt.so.20", Lib)
	Copy("/lib/x86_64-linux-gnu/libgpg-error.so.0", Lib)
	Copy("/lib/x86_64-linux-gnu/libsystemd.so.0", Lib)
	Copy("/lib/x86_64-linux-gnu/libc.so.6", Lib)
	// Copy("", Lib)
	Copy("/lib64/ld-linux-x86-64.so.2", Lib64)
	Copy("~/.bashrc", Home)
}

func Copy(sourcePath string, destDir string) {

	// Open the source file
	sourceFile, _ := os.Open(sourcePath)

	defer sourceFile.Close()

	// Get the destination file path
	destPath := filepath.Join(destDir, filepath.Base(sourcePath))

	// Create the destination file
	destFile, _ := os.OpenFile(destPath, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0755)

	defer destFile.Close()

	// Copy the contents of the source file to the destination file
	io.Copy(destFile, sourceFile)

}
