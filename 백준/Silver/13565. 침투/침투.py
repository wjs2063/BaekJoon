import sys
from _collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []

visited = [[False]*m for _ in range(n)]
for _ in range(n):
    graph.append(input().strip())

def bfs(pos):
    global graph
    global visited
    q = deque([pos])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[pos[0]][pos[1]] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or graph[nx][ny] == '1':continue
            visited[nx][ny] = True
            q.append((nx,ny))

for j in range(m):
    bfs((0,j))
flag = False
for j in range(m):
    if visited[n - 1][j] == True:
        flag = True
        break
if flag:
    print("YES")
else:
    print("NO")


