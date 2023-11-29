import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

m, n = map(int, input().split())

grid = []

for _ in range(n):
    grid.append(input().strip())

vis = set()
res = [0, 0]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(a, b):
    # a,b의 병사와 같은 아군들의 수를 return (자기자신 포함)
    our_team = grid[a][b]
    res = 1
    for (dx, dy) in dirs:
        nx = a + dx
        ny = b + dy
        if not (0 <= nx < n and 0 <= ny < m): continue
        if (nx, ny) in vis: continue
        if grid[nx][ny] != our_team: continue
        vis.add((nx, ny))
        res += dfs(nx, ny)
    return res


for x, row in enumerate(grid):
    for y, col in enumerate(row):
        if (x, y) in vis: continue
        if grid[x][y] == "W":
            vis.add((x,y))
            res[0] += dfs(x, y) ** 2
        else:
            vis.add((x,y))
            res[1] += dfs(x, y) ** 2

print(*res)