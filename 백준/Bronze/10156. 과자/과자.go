package main

import (
	"bufio"
	"fmt"
	"os"
)

/*
과자 k원
사려고하는 과자 n 개
현재가진돈 m
*/

func main() {
	var k, n, m int
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	//var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

	fmt.Fscanln(reader, &k, &n, &m)
	if k*n >= m {
		fmt.Println(k*n - m)
	} else {
		fmt.Println(0)
	}
}
