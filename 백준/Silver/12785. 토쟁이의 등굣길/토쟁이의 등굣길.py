import sys
input = sys.stdin.readline

w,h = map(int,input().split())
y,x = map(int,input().split())

# dp[i][j] i,j 까지 오는 방법수
#[i - 1][j] 에서 오거나 [i][j - 1] 에서 오거나
# [x][y] 필수로 들렀다가 [x][y] 에서 끝점까지
# -------
#-
#-
#-
#-
# 세로가 x 가로가 y
dp = [[0]*w for _ in range(h)]
MOD = int(1e6 + 7)
for i in range(x):
    for j in range(y):
        if i == 0 or j == 0 :
            dp[i][j] = 1
            continue
        dp[i][j] = (dp[i][j] +  dp[i - 1][j] + dp[i][j - 1]) % MOD

for i in range(x - 1,h):
    for j in range(y - 1,w):
        if i == x - 1 or j == y - 1 :
            dp[i][j] = dp[x - 1][y - 1]
            continue
        dp[i][j] = (dp[i][j] + dp[i - 1][j] + dp[i][j - 1]) % MOD
print(dp[-1][-1] % MOD)
