import sys
from _collections import deque
input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

dp = [[0]*n for _ in range(n)]
# 시작점
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] == 1:
            if j + graph[i][j] <= n - 1:
                dp[i][j + graph[i][j]] = 1
            if i + graph[i][j] <= n - 1:
                dp[i + graph[i][j]][j] = 1
if dp[n - 1][n - 1]:
    print("HaruHaru")
else:
    print("Hing")
