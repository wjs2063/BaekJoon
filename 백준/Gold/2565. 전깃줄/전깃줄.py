import sys
input = sys.stdin.readline

n = int(input())

ee = []

for _ in range(n):
    a,b = map(int,input().split())
    ee.append((a,b))
# sorting A
ee.sort(key = lambda x:x[0])

# Longest Consequtive Sequence length

dp = [1]*( n)

for i in range(n):
    for j in range(i):
        if ee[i][1] > ee[j][1] :
            dp[i] = max(dp[i],dp[j] + 1)
print(n - max(dp))