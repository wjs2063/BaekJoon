import sys
input = sys.stdin.readline


n,m,c = map(int,input().split())

W,A,B = [],[],[]

for _ in range(c):
    W.append(list(map(int,input().split())))
dp = [[0]*(m + 1) for _ in range(n + 1)]
# dp[i][j] -> A 의 i번째 인덱스, B 의 j번째 인덱스 까지의 만족도합의 최댓값
A = list(map(int,input().split()))
B = list(map(int,input().split()))

"""
xi,xj 가 악수를 했으면 
yi,yj 
인덱스 -> 증가  
"""
for i in range(1,n + 1):
    for j in range(1,m + 1 ):
        dp[i][j] = max(dp[i][j],dp[i - 1][j],dp[i][j - 1] , dp[i - 1][j - 1] + W[A[i - 1] - 1][B[j - 1] - 1])

print(dp[n][m])
