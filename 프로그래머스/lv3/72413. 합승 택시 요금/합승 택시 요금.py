def solution(n, s, a, b, fares):
    answer = 0
    inf = float("inf")
    dp = [[inf] * (n + 1) for _ in range(n + 1)]
    # dp[a][b] := a 에서 b 로 가는데 소모되는 비용
    for i in range(1,n + 1):
        dp[i][i] = 0
    for c,d,f in fares:
        dp[c][d] = f
        dp[d][c] = f
    # k 를 거쳐 갈수있는곳 모두 조사
    for k in range(1,n + 1):
        for i in range(1,n + 1):
            for j in range(1,n + 1):
                dp[i][j] = min(dp[i][k] + dp[k][j],dp[i][j])
    # s -> a,b 가는 최소비용 
    ans = float("inf")
    for k in range(1,n + 1):
        ans = min(ans,dp[s][k] + dp[k][a] + dp[k][b])
    return ans                