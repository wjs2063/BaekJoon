import sys
input = sys.stdin.readline

n,m = map(int,input().split())

grid = []
coin = []
for i in range(n):
    grid.append(input().strip())
    for j in range(m):
        if grid[i][j] == "o":
            coin.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 11

def in_range(a,b):
    if 0 <= a < n and 0 <= b < m:
        return 1
    return 0

def backtracking(a,b,c,d,cnt):
    global ans
    # 각 4가지 방향에 대해서 전수조사해야함
    if cnt >= 10:
        return

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        ns = c + dx[i]
        nt = d + dy[i]

        if in_range(nx,ny) and grid[nx][ny] == "#":
            nx,ny = a,b
        if in_range(ns,nt) and grid[ns][nt] == "#":
            ns,nt = c,d
        tot = in_range(nx,ny) + in_range(ns,nt)
        if tot == 1:
            ans = min(ans,cnt + 1)
            return
        if tot == 0 : continue
        backtracking(nx,ny,ns,nt,cnt + 1)
x,y = coin[0]
z,w = coin[1]
backtracking(x,y,z,w,0)
if ans == 11:
    print(-1)
else:
    print(ans)
