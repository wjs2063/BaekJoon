import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input().strip())

arr = list(map(int,input().split()))

dp = [arr[0]]

for i in range(n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
    else:
        idx = bisect_left(dp,arr[i])
        dp[idx] = arr[i]
print(len(dp))
