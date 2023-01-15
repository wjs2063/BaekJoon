import sys
from _collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
visited = [[False]*m for _ in range(n)]
cnt = 0
def bfs(graph,i,j):
    global visited
    q = deque([(i,j)])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = (x + dx[i]) % n
            ny = (y + dy[i]) % m
            if not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx,ny))


for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 0:
            cnt += 1
            bfs(graph,i,j)
print(cnt)
