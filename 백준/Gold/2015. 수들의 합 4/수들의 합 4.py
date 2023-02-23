import sys
from collections import defaultdict
input = sys.stdin.readline

n,k = map(int,input().split())

arr = list(map(int,input().split()))

memo = defaultdict(int)

ans = 0
for i in range(1,n):
    arr[i] += arr[i - 1]

for i in range(n):
    if arr[i] == k:
        ans += 1
    # s(j) - s(i - 1) = k
    # s(j) - k = s(i - 1)
    ans += memo[arr[i] - k]
    # 현재 누적합이 되는경우를 추가
    memo[arr[i]] += 1
print(ans)