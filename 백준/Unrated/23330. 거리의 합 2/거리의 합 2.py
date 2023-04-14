import sys
input = sys.stdin.readline

n = int(input())

A = list(map(int,input().split()))

A.sort()

p = [0] + A

n = len(p)

for i in range(1,n):
    p[i] += p[i - 1]

ans = 0

for i in range(1,n):
    k = i - 1
    val = A[k] * (2*k + 2 - (n - 1)) + p[n - 1] -2*p[k + 1]
    ans += val
print(ans)