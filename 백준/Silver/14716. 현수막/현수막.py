import sys 
from collections import deque
input = sys.stdin.readline 

n,m = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))
visited = [[0]*m for _ in range(n)]
    
def bfs(i,j):
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,1,-1,1,-1]
    visited[i][j] = 1
    q = deque([(i,j)])
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] :continue
            if arr[nx][ny] == 0:continue
            visited[nx][ny] = 1
            q.append((nx,ny))
    return 1
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            ans += bfs(i,j)
print(ans)    
    