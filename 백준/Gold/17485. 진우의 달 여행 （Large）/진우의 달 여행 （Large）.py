import sys
si = sys.stdin.readline

n,m = map(int,si().strip().split())

space = []

for _ in range(n):
    data = list(map(int,si().strip().split()))
    space.append(data)
space.append([0] * m)
dp = [[[int(1e10)] * 3 for _ in range(m)] for _ in range(n + 1)]

direction = {
    0:(-1,-1),
    1:(-1,0),
    2:(-1,1)
}


for j in range(m):
    dp[0][j] = [space[0][j]] * 3
for i in range(1,n + 1):
    for j in range(m):
        for d in range(3):
            ni,nj = direction[d]
            bi,bj = i + ni,j + nj
            if not 0 <= bj < m:continue
            for k in range(3):
                if k == d :continue
                dp[i][j][d] = min(dp[i][j][d], dp[bi][bj][k] + space[i][j])

ans = int(1e10)

for j in range(m):
    ans = min(ans,min(dp[n][j]))
print(ans)
