import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(input().strip())


def bfs(i,j):
    visited = [[0]*m for _ in range(n)]
    q = deque([(i,j,0)])
    visited[i][j] = 1
    res = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x,y,cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]: continue
            if arr[nx][ny] == "W":continue
            q.append((nx,ny,cnt + 1))
            if cnt + 1 > res:
                res = cnt + 1
            visited[nx][ny] = 1
    return res

answer = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == "W":continue
        answer = max(answer,bfs(i,j))
print(answer)
