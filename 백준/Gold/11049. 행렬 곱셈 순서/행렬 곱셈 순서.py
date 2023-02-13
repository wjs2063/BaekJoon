import sys
input = sys.stdin.readline

n = int(input().strip())

matrix = []

for _ in range(n):
    matrix.append(list(map(int,input().split())))
INF = float('inf')
dp = [[INF]*(n + 1) for _ in range(n + 1)]

for i in range(n):
    dp[i][i] = 0
    if i + 1 < n:
        dp[i][i + 1] = matrix[i][0] * matrix[i][1] * matrix[i + 1][1]

"""
dp[i][i + 1] :초기화를 시키자

dp[i][j] -> i부터 j 까지 의 연산의 최솟값
dp[i][k] -> i부터 k 까지 연산 최솟값 * dp[k + 1][j] 
"""
# k 는 window size
for k in range(1,n):
    for i in range(n - k):
        for j in range(i,i + k):
            if dp[i][i + k] > dp[i][j] + dp[j + 1][i + k] + matrix[i][0]*matrix[j][1]*matrix[i + k][1]:
                dp[i][i + k] = dp[i][j] + dp[j + 1][i + k] + matrix[i][0]*matrix[j][1]*matrix[i + k][1]

print(dp[0][n - 1])

