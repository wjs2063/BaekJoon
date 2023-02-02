import sys
input = sys.stdin.readline

n = int(input())

L = [0] + list(map(int,input().split()))

J = [0] + list(map(int,input().split()))
dp = [[0]*101 for _ in range(n + 1)]
# dp[i][j] -> i개를 선택 j 라는 체력으로 얻을수있는 최대기쁨
for i in range(1,n + 1):
    # j는 체력이고
    for j in range(1, 101):
        if j - L[i] > 0:
            dp[i][j] = max(dp[i - 1][j],dp[i - 1][j - L[i]] + J[i])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n][100])
