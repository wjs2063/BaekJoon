import sys
from collections import deque
import copy
input = sys.stdin.readline

m = int(input().strip())
graph = []
for _ in range(2):
    graph.append(input().strip())
white = graph[0].count('.') + graph[1].count('.')
# bfs
# 시작가능지점
# 왼쪽에서 오른쪽으로 가는 최단 경로 거리 구하고
# 총 . 개수에서 최단경로 거리 뺴면됨


def bfs(graph):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    INF = int(1e10)
    answer = INF
    for i in range(2):
        if graph[i][0] == '#':
            continue
        visited = [[INF] * m for _ in range(2)]
        visited[i][0] = 1
        q = deque([(i,0)])
        while q:
            x,y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < 2 and 0 <= ny < m and graph[nx][ny] != '#' and visited[nx][ny] == INF:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
        answer = min(visited[0][m - 1],visited[1][m - 1],answer)
    return answer
print(white - bfs(graph))