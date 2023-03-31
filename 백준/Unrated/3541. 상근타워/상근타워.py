import sys
input = sys.stdin.readline
n,m = map(int,input().split())
e = []
for _ in range(m):
    a,b = map(int,input().split())
    e.append((a,b))

ans = int(1e10)


for a,b in e:
    q,r = divmod(a*n,a + b)

    if r == 0:
        y = min(q - 1,n - 1)
        sub = a * n - (a + b) * y
    else:
        y = min(q,n - 1)
        sub = a * n - (a + b) * y
    ans = min(ans,sub)
print(ans)

