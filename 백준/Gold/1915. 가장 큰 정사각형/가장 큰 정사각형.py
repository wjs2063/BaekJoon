import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(input().strip())
dp = [[0]*m for _ in range(n)]
# dp[i][j] := i,j 를 우측하단으로하는 정사각형의 최대변의 길이
res = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            if arr[i][j] == "1":
                dp[i][j] = 1
            if res < dp[i][j]:
                res = dp[i][j]
            continue
        if arr[i][j] == "0":continue
        dp[i][j] = min(dp[i - 1][j - 1],dp[i - 1][j],dp[i][j - 1]) + 1
        if res < dp[i][j]:
            res = dp[i][j]
print(res**2)
