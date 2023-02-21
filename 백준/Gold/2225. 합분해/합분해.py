import sys
input = sys.stdin.readline

n,k = map(int,input().split())

dp = [[0]*(k + 1) for _ in range(n + 1)]
#dp[n][x] x개의 정수를 더해서 n 을 만드는 가지수
MOD = int(1e9)


for i in range(n + 1):
    # 자기자신으로 채우는경우 1 
    dp[i][1] = 1
    for j in range(1,k + 1):
        # 0,1,2,3,,,,9.. n
        for t in range(n + 1):
            if i - t >= 0 :
                dp[i][j] = (dp[i][j] + dp[i - t][j - 1]) % MOD

print(dp[n][k])

