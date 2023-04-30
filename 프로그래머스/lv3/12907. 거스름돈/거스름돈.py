def solution(n, money):
    answer = 0
    dp = [0]*(n + 1)
    dp[0] = 1
    # dp[x]  := x원을 -> 화폐로  거슬러 주는 방법의 수 
    # 1 2 5 
    # x - 1 , x - 2 , x - 5 
    for m in money:
        for i in range(1,n + 1):
            if i - m >= 0:
                dp[i] += dp[i - m]
    return dp[n]