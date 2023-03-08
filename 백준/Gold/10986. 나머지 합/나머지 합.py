import sys
from collections import defaultdict
input = sys.stdin.readline


n,m = map(int,input().split())

arr = list(map(int,input().split()))

memo = defaultdict(int)
for i in range(n):
    if i >= 1:
        arr[i] = (arr[i - 1] + arr[i]) % m
    memo[arr[i] % m] += 1
ans = 0
for rest in range(m):
    # 나머지 rest 가 0일떄는 자기자신도 가능할것이다
    if rest == 0:
        ans += memo[rest]
    ans += memo[rest] * ( memo[rest] - 1) // 2
print(ans)