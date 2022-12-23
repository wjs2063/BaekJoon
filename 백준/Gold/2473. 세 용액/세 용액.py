import sys
input = sys.stdin.readline

n = int(input().strip())

lq = list(map(int,input().split()))

lq.sort()
ans = int(1e11)
a,b,c = 0,0,0

for i in range(n - 2):
    x = lq[i]
    target = -x
    l,r = i + 1, n - 1
    while l < r :
        s = lq[l] + lq[r]
        if abs(s + x) < ans :
            ans = abs(s + x)
            a = x
            b = lq[l]
            c = lq[r]
        if s < target:
            l += 1
        else:
            r -= 1
print(a,b,c)