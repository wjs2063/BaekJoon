import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = []
dp = [[0]*n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input().split())))
# dp[x][y] -> x,y 에서 갈수있는 최댓값

# dfs(x,y) -> x,y 에서 갈수있는 최대거리를 내뿜는다.
def dfs(x,y):
    global dp
    if dp[x][y] :return dp[x][y]
    # 방문한적이없으면 1
    dp[x][y] = 1
    for dx,dy in zip([-1,1,0,0],[0,0,-1,1]):
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[x][y] >= graph[nx][ny] :continue
        # dfs(nx,ny) 의미 -> nx,ny 에서 갈수있는 최댓값이니 거기서 1 더해주어야한다.
        dp[x][y] = max(dp[x][y],dfs(nx,ny) + 1)
    return dp[x][y]
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans,dfs(i,j))
print(ans)
