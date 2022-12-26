import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

r,c,k = map(int,input().split())
graph = []
for _ in range(r):
    graph.append(input().strip())
visited = [[False]*(c) for _ in range(r)]
visited[r-1][0] = True
ans = 0
def sol(graph,visited,sn,cnt):
    global ans
    global k
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    x,y = sn
    if x == 0 and y == c - 1 and cnt == k:
        ans += 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c or graph[nx][ny] == 'T' :continue
        if visited[nx][ny]:continue
        visited[nx][ny] = True
        sol(graph,visited,(nx,ny),cnt + 1)
        visited[nx][ny] = False
sol(graph,visited,(r - 1,0),1)
print(ans)

