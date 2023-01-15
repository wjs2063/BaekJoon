import sys
from _collections import deque
input = sys.stdin.readline

r,c = map(int,input().split())

graph = []
for _ in range(r):
    graph.append(input().strip())

q = set()
path = set({graph[0][0]})
q.add((0,0,graph[0][0]))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 1
while q:
    x,y,path = q.pop()
    for px,py in zip(dx,dy):
        nx = x + px
        ny = y + py
        if nx < 0 or nx >= r or ny < 0 or ny >= c:continue
        if graph[nx][ny] in path:continue
        answer = max(answer,len(path) + 1)
        q.add((nx,ny,path + graph[nx][ny]))
print(answer)