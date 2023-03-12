import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

g = []
for i in range(n):
    g.append(input().strip())
    for j in range(m):
        if g[i][j] == "R":
            rx,ry = i,j
        if g[i][j] == "B":
            bx,by = i,j
        if g[i][j] == "O":
            ox,oy = i,j

def go(x,y,dx,dy):
    ct = 0
    nx,ny = x,y
    while g[nx + dx][ny + dy] != "#" and g[nx][ny] != "O":
        nx += dx
        ny += dy
        ct += 1
    return nx,ny,ct


def bfs(rx,ry,bx,by):
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    vis = [[[[0]*m for _ in range(n)] for _ in range(m)]for _ in range(n)]

    vis[rx][ry][bx][by] = 1
    q = deque([(rx,ry,bx,by,0)])
    while q:
        rx,ry,bx,by,cnt = q.popleft()
        # 10번했는데 안되면
        if cnt >= 10 : return - 1
        for dx,dy in dirs:
            # 해당방향으로 쭉 보내고
            rrx,rry,rcnt = go(rx,ry,dx,dy)
            bbx,bby,bcnt = go(bx,by,dx,dy)
            # 만약 블루가 빠지면안되니 패스
            if (bbx,bby) == (ox,oy):continue
            if (rrx,rry) == (ox,oy):return cnt + 1
            # 이제 겹치는 경우
            if (rrx,rry) == (bbx,bby):
                # 이말은 blue 구슬이 더 적게움직였으니 해당방향에서 앞에있었다는 소리
                if rcnt > bcnt:
                    rrx,rry = rrx - dx,rry - dy
                else:
                    bbx,bby = bbx - dx,bby - dy
            if vis[rrx][rry][bbx][bby]:continue
            vis[rrx][rry][bbx][bby] = 1
            q.append((rrx,rry,bbx,bby,cnt + 1))
    return -1
print(bfs(rx,ry,bx,by))


