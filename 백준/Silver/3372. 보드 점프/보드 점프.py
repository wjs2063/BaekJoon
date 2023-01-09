import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        # 0은 못가는케이스
        if graph[i][j] == 0:
            continue
        dist = graph[i][j]
        # 오른쪽
        if j + dist < n:
            dp[i][j + dist] += dp[i][j]
        # 아래
        if i + dist < n:
            dp[i + dist][j] += dp[i][j]
print(dp[-1][-1])