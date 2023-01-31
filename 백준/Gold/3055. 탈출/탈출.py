import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int,input().split())

graph = []
water = [[(0,-1)]*c for _ in range(r)]
rx,ry = -1,-1
sx,sy = -1,-1

temp = []
# water[i][j] -> bfs 먼저돌려서 물이 찬 시점도 기록하자
for i in range(r):
    graph.append(input().strip())
    for j in range(c):
        # 도착지점
        if graph[i][j] == "D":
            rx,ry = i,j
        # 시작지점
        if graph[i][j] == "S":
            sx,sy = i,j
        # *은 물이있는 지점
        if graph[i][j] == "*":
            temp.append((i,j))
# bfs() -> 물이 차는 지점
# 시복,공복 O(r*c)
def bfs():
    r = len(graph)
    c = len(graph[0])
    q = deque([])
    # 0번째 시점에 다 넣기
    for x,y in temp:
        q.append((x,y,0))
        # x,y 지점에 물이있다는 표시 1 과 시점 0을 기록
        water[x][y] = (1,0)

    while q:
        x,y, time = q.popleft()
        for dx,dy in zip([-1,1,0,0],[0,0,-1,1]):
            nx = x + dx
            ny = y + dy
            # 범위 벗어나면 패스, 돌도 패스,비버지점도 패스
            if nx < 0 or nx >= r or ny < 0 or ny >= c or graph[nx][ny] == "X" or graph[nx][ny] == "D" :continue
            # 이전에 물이찬 지점이라면 패스
            if water[nx][ny][0] == 1:continue
            # nx,ny 에 물표시,시점 넣어주고
            water[nx][ny] = (1,time + 1)
            q.append((nx,ny,time + 1))
# water[x][y] := x,y 시점에 물이 차있을떄 그떄의 시점 기록 (1,4) -> 1이면 물이차있다는 의미, 4라는 시점에 찬다는 의미

# 물에 일단 시점 다 돌려주고
bfs()
def bfs1(sx,sy,rx,ry):
    r,c = len(graph),len(graph[0])
    q = deque([(sx,sy,0)])
    visited = [[0]*c for _ in range(r)]
    visited[sx][sy] = 1
    while q:
        x,y,time = q.popleft()
        for dx,dy in zip([-1,1,0,0],[0,0,-1,1]):
            nx = x + dx
            ny = y + dy
            # 범위벗어나고 돌은 못가고
            if nx < 0 or nx >= r or ny < 0 or ny >= c or graph[nx][ny] == "X" or graph[nx][ny] == "S" :continue
            if visited[nx][ny] :continue
            # 만약 nx,ny에 물이차있고, 다음시점에 물이찰 경우이거나 이미 물이찬경우면
            if water[nx][ny][0] == 1 and water[nx][ny][1] <= time + 1:continue
            # 비버지점이라면 return
            if (nx,ny) == (rx,ry):return time + 1
            visited[nx][ny] = 1
            q.append((nx,ny,time + 1))
    return "KAKTUS"

print(bfs1(sx,sy,rx,ry))