import sys
from _collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

visited = [[False]*m for _ in range(n)]
# bfs 의미 그림의 넓이를 return
def bfs(graph,visited,i,j):
    visited[i][j] = True
    q = deque([(i,j)])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    answer = 1
    while q :
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0 :continue
            if visited[nx][ny] :continue
            visited[nx][ny] = True
            answer += 1
            q.append((nx,ny))
    return answer
cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            cnt += 1
            ans = max(ans,bfs(graph,visited,i,j))
print(cnt)
print(ans)