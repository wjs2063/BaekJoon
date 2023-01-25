import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input().strip())

arr = list(map(int,input().split()))
# sorting -> 순
arr.sort()
x = int(input())

l,r = 0, len(arr) - 1
ans = 0
# 겹치면안되니까
# Two Pointer 칸 증가시키는 기준은?
while l < r:
    # 더해서 x 면 증가 좌우측 증가
    tt = arr[l] + arr[r]
    if tt == x:
        l += 1
        r -= 1
        ans += 1
    elif tt < x:
        l += 1
    else:
        r -= 1
print(ans)
