import sys
input = sys.stdin.readline

n = int(input().strip())

arr = []

dp =[[0]*n for _ in range(n)]

for i in range(n):
    arr.append(list(map(int,input().split())))
    dp[i] = arr[i]
for k in range(n):
    for i in range(n):
        for j in range(n):
            # i 에서 k 를 거쳐 k 에서 j를 거쳐 갈수있다면 i에서 j 로 갈수있게 된다
            if dp[i][k] == 1 and dp[k][j] == 1:
                dp[i][j] = 1
for i in range(n):
    print(*dp[i])
