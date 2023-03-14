import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e10)
dp = [INF]*(n + 1)
dp[0] = 0
dp[1] = 1

for i in range(2,n + 1):
    for k in range(1,int(i**0.5) + 1):
        dp[i] =  min(dp[i],1 + dp[i - k**2])
print(dp[n])