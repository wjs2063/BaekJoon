import sys
from collections import deque
input = sys.stdin.readline

def bfs(s,e):
    # l,r,c
    sx,sy,sz = s
    ex,ey,ez = e
    visited = [[[0]*c for _ in range(r)] for _ in range(l) ]
    visited[sx][sy][sz] = 1
    q = deque([(sx,sy,sz,0)])
    #
    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]
    while q:
        x,y,z,cnt = q.popleft()
        if (x,y,z) == (ex,ey,ez):return cnt
        for i in  range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= r or nz < 0 or nz >= c or visited[nx][ny][nz] :continue
            if arr[nx][ny][nz] == "#":continue
            visited[nx][ny][nz] = 1
            q.append((nx,ny,nz,cnt + 1))
    return -1



while True:
    l,r,c = map(int,input().split())
    if (l,r,c) == (0,0,0):
        break
    arr = []
    for i in range(l):
        temp = []
        for j in range(r):
            temp.append(input().strip())
            for k in range(c):
                if temp[j][k] == "S":
                    s = (i,j,k)
                if temp[j][k] == "E":
                    e = (i,j,k)
        x = input()
        arr.append(temp)
    t = bfs(s,e)
    if t == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {t} minute(s).")


