import sys

si = sys.stdin.readline

r, c, q = map(int, si().split())
arr = []

for _ in range(r):
    arr.append(list(map(int, si().split())))

dp = [[0] * (c + 1) for _ in range(r + 1)]

# dp[i][j] -> 0,0 부터 i,j 까지 직사각형 넓이 -> padding -> 1,1 부터 i,j까지


for row in range(1, r + 1):
    for col in range(1, c + 1):
        dp[row][col] = dp[row][col - 1] + dp[row - 1][col] - dp[row - 1][col - 1] + arr[row - 1][col - 1]

for _ in range(q):
    r1, c1, r2, c2 = map(int, si().split())


    n = abs(r2 - r1 + 1) * abs(c2 - c1 + 1)
    area = dp[r2][c2] - dp[r2][c1 - 1] - dp[r1 - 1][c2] + dp[r1 - 1][c1 - 1]

    print(area // n)