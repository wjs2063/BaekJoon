import sys
input = sys.stdin.readline
n = int(input().strip())

grid = []
# input
for _ in range(n):
    grid.append(list(map(int,input().split())))
p = [[0]*(n + 1) for _ in range(n + 1)]

for row in range(1,n + 1):
    for col in range(1,n + 1):
        p[row][col] = p[row - 1][col] + p[row][col - 1] - p[row - 1][col - 1] + grid[row - 1][col - 1]
ans = int(-1e5)
for width in range(n):
    for sr in range(1,n - width + 1):
        for sc in range(1,n - width + 1):
            res = p[sr + width][sc + width] - p[sr + width][sc - 1] - p[sr - 1][sc + width] + p[sr - 1][sc - 1]
            ans = max(ans,res)

print(ans)