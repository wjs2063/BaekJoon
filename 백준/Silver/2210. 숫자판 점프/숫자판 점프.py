import sys
from collections import deque
input = sys.stdin.readline

arr = []

for _ in range(5):
    arr.append(input().split())


def bfs():
    q = deque([])
    for i in range(5):
        for j in range(5):
            q.append((i,j,arr[i][j]))
    #
    visited = set()
    while q :
        x,y,temp = q.popleft()
        if len(temp) == 6:
            visited.add(temp)
            continue
        for dx,dy in zip([-1,1,0,0],[0,0,-1,1]):
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 :continue
            if temp + arr[nx][ny] in visited:continue
            q.append((nx,ny,temp + arr[nx][ny]))
    return len(visited)

print(bfs())