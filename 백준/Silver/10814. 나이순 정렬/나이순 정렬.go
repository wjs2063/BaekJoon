package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

type Member struct {
	age  int
	name string
	time int
}

func main() {

	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int = 0
	fmt.Fscanln(reader, &n)
	// 2
	var age int
	var name string
	// make slice
	members := make([]Member, 0, n)
	// input members
	for i := 0; i < n; i++ {
		fmt.Fscanln(reader, &age, &name)
		members = append(members, Member{age: age, name: name, time: i})
	}
	// 먼저 가입한순서
	sort.SliceStable(members, func(i, j int) bool {
		return members[i].time < members[j].time
	})

	// 먼저 나이순으로 정렬한번
	sort.SliceStable(members, func(i, j int) bool {
		return members[i].age < members[j].age
	})

	for _, v := range members {
		fmt.Fprintln(writer, strconv.Itoa(v.age), v.name)
	}
}
