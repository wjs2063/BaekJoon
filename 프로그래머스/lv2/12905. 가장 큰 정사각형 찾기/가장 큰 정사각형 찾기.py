def solution(board):
    ans = 0 
    n = len(board)
    m = len(board[0])
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1,n + 1):
        for j in range(1,m + 1):
            if board[i - 1][j - 1]:
                dp[i][j] = 1
    # dp[i][j] := i ,j 를 우하단으로 하는 정사각형의 최대길이 
    for i in range(1,n + 1):
        for j in range(1,m + 1):
            if board[i - 1][j - 1] == 1 :
                # 3개의 를 확인해야함 
                dp[i][j] = min(dp[i - 1][j - 1],dp[i - 1][j],dp[i][j - 1]) + 1
            ans = max(ans,dp[i][j] ** 2)
    return ans