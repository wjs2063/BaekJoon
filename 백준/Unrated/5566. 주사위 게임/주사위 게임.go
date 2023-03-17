package main

import (
	"fmt"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	var n, m, ans, now int
	var temp int
	arr := []int{0}
	command := []int{}
	now = 1
	fmt.Scanln(&n, &m)
	for i := 0; i < n; i++ {
		fmt.Scanln(&temp)
		arr = append(arr, temp)

	}
	for i := 0; i < m; i++ {
		fmt.Scanln(&temp)
		command = append(command, temp)
	}
	for i := 0; i < m; i++ {
		now = min(n, now+command[i])
		now = min(n, now+arr[now])
		if now >= n {
			ans = i + 1
			break
		}
	}
	fmt.Println(ans)

}
