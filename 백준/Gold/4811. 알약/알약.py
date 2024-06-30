import sys

si = sys.stdin.readline

dp = [[0] * 31 for _ in range(31)]

for i in range(1,30 + 1):
    dp[0][i] = 1

for w in range(1,30 + 1):
    for h in range(30):
        if h == 0 :
            dp[w][h] = dp[w - 1][h + 1]
        else:
            dp[w][h] = dp[w - 1][h + 1] + dp[w][h - 1]


while True:
    n = int(si().strip())
    if n == 0:
        break
    print(dp[n][0])
    """
    10알 
    1조각 W 반조각 H 
    
     
    """
