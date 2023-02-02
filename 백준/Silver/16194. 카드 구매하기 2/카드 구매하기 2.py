import sys
input = sys.stdin.readline

n = int(input().strip())

arr = [0] + list(map(int,input().split()))

dp = [0] + [arr[i] for i in range(1,n + 1)]

for i in  range(1, n + 1):
    for j in range(1,i):
        dp[i] = min(dp[i],dp[i - j] + arr[j])
print(dp[n])