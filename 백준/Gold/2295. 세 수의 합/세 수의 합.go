package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

/*
주어진 집합을 T 라하자
T의 원소를 t 라두면

x + y + z = t 를 만족하는 t 의 최댓값을 찾는게 목표다

주어진조건은 N^2 logN 이내로 풀어야하는 문제이므로
x + y = t - z 로 두자

x + y 로 가능한 모든 경우의 수를 구한다.

그리고 또한 t - z 로 이중반복문을돌면서 이분탐색으로 x + y 집합의 원소와 매칭되는것을 찾는다.
혹은 map 을 사용해서 존재하는지 체크한다. 본인 취향대로

*/

func BinarySearch(target int64, slice []int64) bool {
	var sn, en int = 0, len(slice) - 1

	for sn <= en {
		mid := (sn + en) / 2

		if slice[mid] == target {
			return true
		} else if slice[mid] < target {
			sn = mid + 1
		} else {
			en = mid - 1
		}
	}
	return false
}

func main() {

	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	slice := make([]int64, 0, 1000)
	var n, i, j, val int64
	var ans int64 = 0
	fmt.Fscanln(reader, &n)

	for i = 0; i < n; i++ {
		fmt.Fscanln(reader, &val)
		slice = append(slice, val)
	}

	add_slice := make([]int64, 0, 1000000)

	for i = 0; i < n; i++ {
		for j = 0; j < n; j++ {
			add_slice = append(add_slice, slice[i]+slice[j])
		}
	}

	sort.Slice(add_slice, func(i, j int) bool {
		return add_slice[i] < add_slice[j]
	})

	for i = 0; i < n; i++ {
		for j = 0; j < n; j++ {
			var target int64 = slice[i] - slice[j]
			// s 가 add_slice 내에 존재하는지 확인해야한다
			if BinarySearch(target, add_slice) {
				if slice[i] > ans {
					ans = slice[i]
				}
			}

		}
	}

	fmt.Println(ans)
}
