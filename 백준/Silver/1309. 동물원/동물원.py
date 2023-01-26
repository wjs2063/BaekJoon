import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [[0,0,0] for _ in range(n + 1)]
# dp[i][0] -> i 번쨰 행에 사자가없는경우
# dp[i][1] -> i 번째 행에 사자가왼쪽에 있는경우
# dp[i][2] -> i 번째 행에 사자가 오른쪽에 있는경우

dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1
MOD = 9901
for i in range(2, n + 1):
    dp[i][0] = sum(dp[i - 1]) % MOD
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % MOD

print(sum(dp[n] ) % MOD)