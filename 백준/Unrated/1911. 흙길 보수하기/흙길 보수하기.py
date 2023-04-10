import sys
input = sys.stdin.readline

n,l = map(int,input().split())

a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

a.sort()

ans = 0
en = 0

for s,e in a:

    if en < s :
        t = (e - s - 1) // l + 1
        en = s + l * t
        ans += t
    elif en < e :
        t = (e - en - 1) // l + 1
        en = en + l * t
        ans += t
print(ans)
