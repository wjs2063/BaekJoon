import sys
input = sys.stdin.readline

w,h = map(int,input().split())

MOD = int(1e5)

dp = [[[0,0] for _ in range(h + 1)] for _ in range(w + 1)]

dp[1][1] = [1,1]

for r in range(1,w + 1):
    for c in range(1,h + 1):
        if r == 1 and c == 1:continue

        dp[r][c][0] = (dp[r][c - 1][0]+dp[r - 1][c - 1][1]) % MOD;
        dp[r][c][1] = (dp[r - 1][c][1]+dp[r - 1][c - 1][0]) % MOD;

print(sum(dp[w][h]) % MOD)