import sys
input = sys.stdin.readline

n,m = map(int,input().split())

cost = [[] ]

for _ in range(n):
    x = [0] + list(map(int,input().split()))
    cost.append(x)

# dp[i][j] -> i 에서 j 까지 가는데 걸리는 최단 시간
# cost[i][j] -> i 에서 j 까지 가는데 (직접 연결된 도로로 가는데 걸리는 시간)

# O(N^3) S:O(N^2)
def floyd():
    INF = int(1e10)
    dp = [[INF]*(n + 1) for _ in range(n + 1)]
    # dp 초기화 dp[x][x] 는 0으로 -> [i][j] 는 cost [i][j]로초기화
    for i in range(1, n + 1):
        for j in range(1,n + 1):
            if i == j :
                dp[i][j] = 0
            else:
                dp[i][j] = cost[i][j]
    # 거쳐가는 지점
    for k in range(1,n + 1):
        for i in range(1,n + 1):
            for j in range(1,n + 1):
                # i 에서 k 를 거쳐 j 로가는게 더빠를수도있잖아?
                dp[i][j] = min(dp[i][j],dp[i][k] + dp[k][j])
    return dp

dp = floyd()

for _ in range(m):
    a,b,c = map(int,input().split())
    if dp[a][b] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")

