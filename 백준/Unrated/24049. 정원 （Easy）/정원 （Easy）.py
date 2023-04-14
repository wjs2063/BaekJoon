import sys
input = sys.stdin.readline

n,m = map(int,input().split())

row = list(map(int,input().split()))
col = list(map(int,input().split()))

grid = [[-1]*(m + 1 ) for _ in range(n + 1)]

for i in range(1,n + 1):
    grid[i][0] = row[i - 1]
for i in range(1,m + 1):
    grid[0][i] = col[i - 1]

for i in range(1,n + 1):
    for j in range(1,m + 1):
        l = grid[i][j - 1]
        r = grid[i - 1][j]
        if l == r:
            grid[i][j] = 0
        else:
            grid[i][j] = 1
print(grid[n][m])