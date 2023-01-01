import sys
input = sys.stdin.readline

# i - 1, i , i + 1 번쨰 카운팅했는지 check

vip = []

n = int(input().strip())
m = int(input().strip())
dp = [0]*(n + 3)
for _ in range(m):
    x = int(input().strip())
    vip.append(x)
# 초기화
dp[0] = 1
dp[1] = 1
# i번쨰 사람이 i 번쨰 않는경우 -> dp[i - 1]
# i번쨰 사람이 i -1 번쨰에 앉는경우 -> dp[i - 2]
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
# vip 좌석
if len(vip) == 0:
    print(dp[n])
else:
    last = 0
    answer = 1
    for v in vip:
        answer *= dp[v - 1 - last]
        last = v
    answer *= dp[n - last]
    print(answer)