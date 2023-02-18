import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    coins = list(map(int,input().split()))
    m = int(input().strip())
    dp = [0]*(m + 1)
    dp[0] = 1
    # dp[x] := n가지동전으로 x원을 만들수있는 총 경우의수
    # 각코인으로 만들수있는 금액은 다 1로
    for coin in coins:
        if coin > m:continue
        for i in range(coin,m + 1):
            dp[i] += dp[i - coin]

    """
    for i in range(m + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] += dp[i - coin]
    """

    print(dp[m])