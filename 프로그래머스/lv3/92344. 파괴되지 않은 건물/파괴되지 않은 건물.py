def solution(board, skill):
    answer = 0
    n,m = len(board),len(board[0])
    dp = [ [0]*(m + 1) for _ in range(n + 1)]
    
    for sk in skill:
        tp,r1,c1,r2,c2,degree = sk
        if tp == 1:
            degree = -degree
        dp[r1][c1] += degree
        dp[r1][c2 + 1] += -degree
        dp[r2 + 1][c1] += -degree
        dp[r2 + 1][c2 + 1] += degree
    # 열방향 
    for i in range(n + 1):
        for j in range(1,m + 1):
            dp[i][j] += dp[i][j - 1]
    # 행방향
    for i in range(1,n + 1):
        for j in range(m + 1):
            dp[i][j] += dp[i - 1][j]
    for i in range(n):
        for j in range(n):
            board[i][j] += dp[i][j]
            if board[i][j] > 0:
                answer += 1
            
    return answer