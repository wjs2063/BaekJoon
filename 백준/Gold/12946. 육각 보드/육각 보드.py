import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = []

# 방문체크 혹은 컬러표시할 배열
color = [[0]*n for _ in range(n)]
# color[i][j] i,j 에 칠한 색깔
visited = [[0]*n for _ in range(n)]
for _ in range(n):
    graph.append(input().strip())

# 모든 세계지도는 3가지색으로 칠할수있음
# 답은 1 or 2 or 3인것은 확실함
ans = 0
def dfs(s,co):
    x,y = s
    # 색칠하기
    color[x][y] = co
    # 방향벡터
    global ans
    # 최소한 1개는 필요해
    ans = max(ans,1)
    dirs = [(-1,0),(0,-1),(1,-1),(1,0),(0,1),(-1,1)]
    for dx,dy in dirs:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >=n or ny < 0 or ny >= n or graph[nx][ny] == "-":continue
        #색칠해야하는곳이고 색칠은 안한경우면
        if graph[nx][ny] == "X" and color[nx][ny] == 0:
            # 최소한 2개는 필요한경우
            ans = max(ans,2)
            if co == 1:dfs((nx,ny),2)
            elif co == 2:dfs((nx,ny),1)
        # 주변칸이 현재와 같은 색이라면?
        if graph[nx][ny] == "X" and color[nx][ny] == co:
            ans = max(ans,3)



for i in range(n):
    for j in range(n):
        # 색칠해야하는곳이면서 색칠안한곳이면 dfs수행
        if graph[i][j] == "X" and color[i][j] == 0:
            dfs((i,j),1)
print(ans)
