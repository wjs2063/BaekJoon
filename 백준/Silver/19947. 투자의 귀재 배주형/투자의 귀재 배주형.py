import sys
input = sys.stdin.readline

h,y = map(int,input().split())

dp = [0] * (11)
dp[0] =  h

for year in range(1,y + 1):
    if year - 1 >= 0 :
        dp[year] = max(dp[year], int(dp[year - 1] * 1.05))
    if year - 3 >= 0:
        dp[year] = max(dp[year],int(dp[year - 3] * 1.2))
    if year - 5 >= 0:
        dp[year] = max(dp[year],int(dp[year - 5] * 1.35))
print(dp[year])