import sys
from _collections import deque
input = sys.stdin.readline

n = int(input().strip())

graph = []

for _ in range(n):
    graph.append(input().strip())
# 0은 미방문 , 1은 방문
visited = [[0]*n for _ in range(n)]

# 단지수 cnt, 단지내 집의수
cnt = 0
ans = []
def bfs(graph,start):
    global visited
    sx,sy = start
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    # 방문체크와 단지내 집 개수 house
    house = 1
    visited[sx][sy] = 1
    q = deque([(sx,sy)])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >=n or visited[nx][ny] or graph[nx][ny] == '0':continue
            visited[nx][ny] = 1
            house += 1
            q.append((nx,ny))
    return house

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == '1':
            cnt += 1
            ans.append(bfs(graph,(i,j)))
# 정렬
ans.sort()
print(cnt)
for i in range(len(ans)):
    print(ans[i])

