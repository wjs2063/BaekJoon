package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
	"strings"
)

func main() {
	var n int
	q := list.New()
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	//var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	slice := make([]string, 0, n)
	fmt.Fscanln(reader, &n)
	var strs string
	for i := 0; i < n; i++ {
		strs, _ = reader.ReadString('\n')
		slice = append(slice, strings.TrimSpace(strs))
	}
	for _, v := range slice {
		s := strings.Split(v, " ")
		if len(s) == 1 {
			//fmt.Println("길이 1  첫번째값 : ", len(s[0]))
			//fmt.Println(s[0] == "pop_front")
			switch s[0] {
			case "pop_front":
				if q.Len() == 0 {
					fmt.Println(-1)
				} else {
					fmt.Println(q.Front().Value)
					q.Remove(q.Front())
				}
			case "pop_back":
				if q.Len() == 0 {
					fmt.Println(-1)
				} else {
					fmt.Println(q.Back().Value)
					q.Remove(q.Back())
				}
			case "size":
				fmt.Println(q.Len())
			case "empty":
				if q.Len() == 0 {
					fmt.Println(1)
				} else {
					fmt.Println(0)
				}
			case "front":
				if q.Len() == 0 {
					fmt.Println(-1)
				} else {
					fmt.Println(q.Front().Value)
				}
			case "back":
				if q.Len() == 0 {
					fmt.Println(-1)
				} else {
					fmt.Println(q.Back().Value)
				}
			}

		} else {
			//fmt.Println("길이 2 값 ", s[0], s[1])
			switch s[0] {
			case "push_front":
				q.PushFront(s[1])
			case "push_back":
				q.PushBack(s[1])
			}
		}

	}

}
