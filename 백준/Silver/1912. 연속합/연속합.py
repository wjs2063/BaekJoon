import sys
input = sys.stdin.readline

n = int(input().strip())
NF = int(-1e4)
arr = list(map(int,input().split()))

dp = [NF]*(n + 1)
#dp[i] := i 번째까지의 연속합중 최댓값
#a0 + a1 + . . . ai
# a1 + a2 ... ai
# a2 + a3 ... ai
# ai 만 뺴보면
# dp[i - 1] + a[i] 가된다
for i in range(1,n + 1):
    dp[i] = max(dp[i - 1] + arr[i - 1],arr[i - 1])
print(max(dp))