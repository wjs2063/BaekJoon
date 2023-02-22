import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[0]*m]
for _ in range(n):
    arr.append([0] + list(map(int,input().split())))
dp = [[0]*(m + 1) for _ in range(n + 1)]
# dp[i][j] : 1,1, ~ i,j 까지 누적합
# dp[i][j] -> dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + arr[i][j]

for i in range(1,n + 1):
    for j in range(1,m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + arr[i][j]
t = int(input().strip())

for _ in range(t):
    i,j,x,y = map(int,input().split())
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])