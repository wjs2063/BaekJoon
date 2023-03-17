package main

import (
	"fmt"
)

func main() {
	var a int
	var b int
	_, err := fmt.Scan(&a, &b)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(a + b)
	}

}
