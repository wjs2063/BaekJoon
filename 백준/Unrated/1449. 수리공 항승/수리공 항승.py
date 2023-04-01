import sys
input = sys.stdin.readline

n,l = map(int,input().split())

pos = list(map(int,input().split()))

pos.sort()

ans = 1
r = pos[0] + l - 1
for i,v in enumerate(pos):
    if v <= r: continue
    ans += 1
    r = v + l - 1

print(ans)
    