package main

import (
	"fmt"
	"os"
	"os/exec"
	"syscall"
)

func main() {
	switch os.Args[1] {
	case "run":
		namespace()
	default:
		panic("bad command")

	}
}

func namespace() {
	fmt.Printf("Running %v\n", os.Args[2:])

	//define command
	cmd := exec.Command(os.Args[2], os.Args[3:]...)

	// set the standard input, output, and error streams of the command
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	// system-specific attributes for the process
	cmd.SysProcAttr = &syscall.SysProcAttr{
		Cloneflags: syscall.CLONE_NEWUTS,
	}
	// Run command
	cmd.Run()

}
