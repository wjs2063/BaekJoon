import sys
input = sys.stdin.readline

n,l = map(int,input().split())

arr = []

for _ in range(n):
    d,r,g = map(int,input().split())
    arr.append((d,r,g))

pos,time = 0,0


for d,r,g in arr:
    # d 까지오는데 걸리는시간
    time += d - pos
    #
    pos = d
    rest = time % (r + g)
    if rest < r:
        # 빨간불이니 기다려
        time += r - rest
time += l - pos

print(time)