import sys
input = sys.stdin.readline

n = int(input())

score = [0] + list(map(int,input().split()))

dp = [0] * (n + 1)
# dp[i] -> 0 ~ i 까지 조가 잘짜여진 정도의 최댓값

for i in range(1,n + 1):
    for j in range(1,i + 1):
        dp[i] = max(dp[i],dp[j - 1] + max(score[j : i + 1]) - min(score[j : i + 1]))
print(dp[n])
