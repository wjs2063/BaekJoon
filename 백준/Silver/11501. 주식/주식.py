import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    r_max = 0
    res = 0
    for i in range(n - 1,-1,-1):
        r_max = max(r_max,arr[i])
        res += r_max - arr[i]
    print(res)
