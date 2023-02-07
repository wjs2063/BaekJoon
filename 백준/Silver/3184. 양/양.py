import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int,input().split())

graph = []

for _ in range(r):
    graph.append(input().strip())

visited = [[0]*c for _ in range(r)]

def bfs(i,j):
    q = deque([(i,j)])
    visited[i][j] = 1
    w = 0
    s = 0
    if graph[i][j] == "o": s += 1
    if graph[i][j] == "v": w += 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 방문했거나 범위 벗어났으면 패스
            if nx < 0 or nx >= r or ny < 0 or ny >= c or visited[nx][ny]:continue
            # 울타리 안돼
            if graph[nx][ny] == "#" : continue
            if graph[nx][ny] == "o":s += 1
            if graph[nx][ny] == "v":w += 1
            visited[nx][ny] = 1
            q.append((nx,ny))
    if s > w :
        w = 0
    else:
        s = 0
    return s,w

wolf = 0
sheep = 0


for i in range(r):
    for j in range(c):
        if not visited[i][j] and graph[i][j] != "#":
            s,w = bfs(i,j)
            wolf += w
            sheep += s
print(sheep,wolf)