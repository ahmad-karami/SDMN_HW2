package main

import (
	"fmt"
	//"io"
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
		extractFile(os.Args[1])

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
	os.RemoveAll(dir)

	os.Mkdir(dir, 0777)

	// ioutil.WriteFile(filepath.Join(dir, "/pids.max"), []byte("20"), 0700)
	ioutil.WriteFile(filepath.Join(dir, "/memory.max"), []byte(M_max+"M"), 0700)
	ioutil.WriteFile(filepath.Join(dir, "/notify_on_release"), []byte("1"), 0700)
	ioutil.WriteFile(filepath.Join(dir, "/cgroup.procs"), []byte(strconv.Itoa(os.Getpid())), 0700)

}

// func Dir(Container string) {

// 	Bin := Container + "/bin"
// 	// Lib := Container + "/lib/x86_64-linux-gnu"
// 	Lib := Container + "/lib/x86_64-linux-gnu/"

// 	// exec files what we need in new root file system
// 	Copy("/bin/ip", Bin)

// 	// library files for exec files
// 	// libc.so.6
// 	// /lib/x86_64-linux-gnu/
// 	Copy("/lib/x86_64-linux-gnu/libbpf.so.0", Lib)
// 	Copy("/lib/x86_64-linux-gnu/libelf.so.1", Lib)
// 	Copy("/lib/x86_64-linux-gnu/libmnl.so.0", Lib)
// 	Copy("/lib/x86_64-linux-gnu/libbsd.so.0", Lib)
// 	Copy("/lib/x86_64-linux-gnu/libcap.so.2", Lib)
// 	// Copy("/lib/x86_64-linux-gnu/libc.so.6", Lib)
// 	// Copy("/lib/x86_64-linux-gnu/libz.so.1", Lib)
// 	Copy("/lib/x86_64-linux-gnu/libmd.so.0", Lib)
// 	// Copy("", Lib)
// }

// func Copy(sourcePath string, destDir string) {

// 	// Open the source file
// 	sourceFile, _ := os.Open(sourcePath)

// 	defer sourceFile.Close()

// 	// Get the destination file path
// 	destPath := filepath.Join(destDir, filepath.Base(sourcePath))

// 	// Create the destination file
// 	destFile, _ := os.OpenFile(destPath, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0755)

// 	defer destFile.Close()

// 	// Copy the contents of the source file to the destination file
// 	io.Copy(destFile, sourceFile)
// }

func file_sys() {
	path := "/home/mr_king/projects/SDMN/"
	file_path := "/home/mr_king/projects/SDMN/ubuntu-base-20.04.2-base-amd64.tar.gz"
	file_url := "http://cdimage.ubuntu.com/ubuntu-base/releases/20.04/release/ubuntu-base-20.04.2-base-amd64.tar.gz"
	if _, err := os.Stat(file_path); os.IsNotExist(err) {
		fmt.Printf("ubuntu:20.04 Filesys does not exist\n")
		cmd := exec.Command("wget", "-P", path, file_url)
		cmd.Run()
		fmt.Printf("File downloaded\n")
	} //else {
	// 	fmt.Printf("ubuntu:20.04 Filesys exists\n")
	// }
}

func extractFile(Container string) {
	file_sys()
	os.Mkdir(Container, 0777)
	file_path := "/home/mr_king/projects/SDMN/ubuntu-base-20.04.2-base-amd64.tar.gz"
	// fmt.Printf("Extracting file %s to %s...\n", file_path, Container)

	// Use tar to extract the file
	cmd := exec.Command("tar", "xzvf", file_path, "-C", Container)
	// -xzf
	cmd.Run()

	fmt.Printf("File %s extracted successfully!\n", Container)
	// Dir(Container)
}

// libelf.so.1
