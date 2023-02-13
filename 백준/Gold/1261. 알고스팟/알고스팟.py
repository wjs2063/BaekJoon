import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(input().strip())

#dp[i][j] -> i,j 까지오는데 벽을 부순 개수

# dp[nx][ny] = min(dp[x][y],

def bfs():
    q = deque([(0,0)])
    INF = (int(1e10))
    # dp[i][j] -> i,j 까지 오는데 필요한 벽의 개수
    dp = [[INF]*m for _ in range(n)]
    dp[0][0] = 0
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    if (0,0) == (n,m) :return 0
    # 먼저 뚫려있는곳을 간다
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] :continue
            # 해당 좌표가 벽일경우 뚫고
            if arr[nx][ny] == "1":
                dp[nx][ny] = min(dp[x][y],dp[x][y]) + 1
                q.append((nx,ny))
            # 아닐경우 그대로 진행
            else:
                dp[nx][ny] = min(dp[x][y],dp[nx][ny])
                q.appendleft((nx,ny))
            visited[nx][ny] = 1
    return dp[n - 1][m - 1]
print(bfs())


