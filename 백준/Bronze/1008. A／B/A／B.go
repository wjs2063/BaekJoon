package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var a, b float64
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

	fmt.Fscanln(reader, &a, &b)
	fmt.Println(a / b)
	fmt.Fprintln(writer, a/b)
}
