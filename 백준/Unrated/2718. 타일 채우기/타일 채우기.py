import sys
input = sys.stdin.readline


t = int(input())

"""
r0 #######
r1 #####
r2 #####
r3 #######
"""

def solve(n):
    dp = [0] *(n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n + 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        for k in range(2,n + 1):
            if i - k >= 0:
                dp[i] += 2*dp[i - k]
        for k in range(2,n + 1,2):
            if i - k >= 0:
                dp[i] += dp[i - k]
    return dp[n]

for _ in range(t):
    n = int(input())
    print(solve(n))