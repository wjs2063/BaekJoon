import sys

si = sys.stdin.readline

n, m = map(int, si().split())
arr = []

for _ in range(n):
    arr.append(int(si().strip()))

arr.sort()

l, r = 0, 0
ans = int(1e10)
n = len(arr)
while l < n and r < n:
    diff = abs(arr[r] - arr[l])
    if diff < m:
        r += 1

    if diff >= m:
        ans = min(ans, diff)
        l += 1
    if l > r:
        l, r = r, l

if r >= n:
    r = n - 1
    for i in range(l, n):
        if abs(arr[i] - arr[r]) >= m: ans = min(ans, abs(arr[i] - arr[r]))

if l >= n:
    l = n - 1
    for i in range(r, n):
        if abs(arr[i] - arr[r]) >= m: ans = min(ans, abs(arr[i] - arr[r]))

print(ans)
