def solution(k, ranges):
    ans = []
    y = [k]
    while k > 1:
        if k % 2 == 0:
            k //= 2
            y.append(k)
        else:
            k = 3 * k + 1
            y.append(k)
    n = len(y)
    # y 좌표 
    dp = [0] * (n)
    # dp[i] := i번째 정적분 값  
    for i in range(1,n):
        dp[i] = (y[i - 1] + y[i]) / 2
        dp[i] += dp[i - 1]
    for sn,en in ranges:
        en = n - 1 + en 
        if sn > en :
            ans.append(-1)
        else:
            ans.append(dp[en] - dp[sn])
        
    return ans