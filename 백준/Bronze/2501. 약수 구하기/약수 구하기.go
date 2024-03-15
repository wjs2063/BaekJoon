package main

import (
	"bufio"
	"fmt"
	"os"
)

/*
자연수 n,k
n의 약수들중 k 번째로 작은수
단 약수가 k 개보다 작다면 0
*/

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var n, k int
	var factorList = make([]int, 0)

	fmt.Fscanln(reader, &n, &k)

	for i := 1; i <= n; i++ {
		if n%i == 0 {
			factorList = append(factorList, i)
		}
	}
	//fmt.Println(factorList)
	if len(factorList) < k {
		fmt.Println(0)
	} else {
		fmt.Println(factorList[k-1])
	}

}