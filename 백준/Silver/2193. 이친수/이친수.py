import sys
input = sys.stdin.readline

n = int(input().strip())

# n 자리 이친
# 0 과 1로만 이루어져있다.
# 무조건 1로 시작하고
# 1 이 두번 연속으로 나타나지않는다.
# 1 이 왔을떄는 무조건 0 이와야한다
# 0 이왔을때는 0 or 1 이올수있다
# 0 + 10
# dp[i][j] -> i 자리 이며 j 로 시작하는 이친수 개수
# dp[i][1] := i 자리이며 1로 시작하는 이친수 1에다가 -> dp[i - 1][0] 붙히면댐
# dp[i][0] := i 자리이며 0 으로 시작하는 이친수 0 에다가 -> dp[i - 1][0] dp[i - 1][1] 둘다가능

dp = [[0,0] for _ in range(n + 1)]

dp[1][0] = 1
dp[1][1] = 1

for i in range(2,n + 1):
    dp[i][1] = dp[i - 1][0]
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
print(dp[n][1])
# dp[n][1] 이 답이다
