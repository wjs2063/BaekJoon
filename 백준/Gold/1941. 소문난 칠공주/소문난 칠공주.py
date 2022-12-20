import sys
from itertools import combinations
from _collections import deque
input = sys.stdin.readline

ccc = combinations([(i,j) for i in range(5) for j in range(5)],7)

graph = []

for _ in range(5):
    graph.append(input().strip())

def check_more_than_four(graph,cc):
    cnt = 0
    for c in cc:
        x,y = c
        if graph[x][y] == 'S':
            cnt += 1
    return True if cnt >=4 else False

def bfs(cc):
    visited = [False] * 7
    q = deque([cc[0]])
    visited[0] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx,ny) in cc:
                nxt = cc.index((nx,ny))
                if not visited[nxt]:
                    q.append((nx,ny))
                    visited[nxt] = True
    return sum(visited) == 7



answer = 0
for cc in ccc:
    if check_more_than_four(graph,cc) and bfs(cc):
        answer += 1
print(answer)
