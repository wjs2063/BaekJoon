import sys
input = sys.stdin.readline
from collections import defaultdict,Counter
n = int(input())

arr = list(map(int,input().split()))
# 정렬해주고
arr.sort()
ans = 0
for i,target in enumerate(arr):
    # 합 target
    sub = arr[:i] + arr[i + 1:]
    l,r = 0,len(sub) - 1
    while l < r :
        s = sub[l] + sub[r]
        if s < target :
            l += 1
        elif s > target:
            r -= 1
        else:
            ans += 1
            break 

print(ans)