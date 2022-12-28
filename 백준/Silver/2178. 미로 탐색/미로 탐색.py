import sys
from _collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(input().strip())

# 1은 이동할수있음 , 0 은 못감

# 시간복잡도 O(N) 공간복잡도 O(N^2)
def bfs(graph):
    sx,sy = 0,0
    n,m = len(graph),len(graph[0])
    # 방문 체크 와 동시에 거리 계산
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    q = deque([(sx,sy)])
    # 방향 벡터
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 벗어나거나 못가는 막혀있으면 pass
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1 or graph[nx][ny] == '0':continue
            #방문했으면 pass
            if visited[nx][ny]:continue
            # 거리 추가
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny))
    return visited[-1][-1]

print(bfs(graph))

# 시간복잡도 O(N) 공간복잡도 O(N^2)