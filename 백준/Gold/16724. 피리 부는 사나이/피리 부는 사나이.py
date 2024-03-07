import sys
sys.setrecursionlimit(10**6)
si = sys.stdin.readline

n, m = map(int, si().split())

grid = []

for _ in range(n):
    grid.append(si().strip())

# find cycle

direction = {
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0)
}
vis = [[0] * m for _ in range(n)]
ans = 0


# 더이상 갈곳이없는경우 -> + 1
# 순환되는 cycle인경우 -> + 1


def dfs(i, j, path: set):
    global ans, vis, grid
    n, m = len(grid), len(grid[0])
    ni, nj = i + direction[grid[i][j]][0], j + direction[grid[i][j]][1]
    if not (0 <= ni < n and 0 <= nj < m):
        vis[ni][nj] = ans + 1
        # 이전 path 모두 동일한 집합임을 의미
        for (x, y) in path:
            vis[x][y] = ans + 1
        ans += 1
        return
    if (ni, nj) in path:
        # 이미 왔던적이있으면 지나온 패스또한 모두 vis[ni][nj] 와 동일한 집합임을 의미
        for (x, y) in path:
            vis[x][y] = ans + 1
        ans += 1
        return
    if vis[ni][nj]:
        for (x, y) in path:
            vis[x][y] = vis[ni][nj]
        return
    return dfs(ni, nj, path | {(i,j)})


for r in range(n):
    for c in range(m):
        if vis[r][c]: continue
        dfs(r, c, set())
        # 해당 방향으로 쭉 진행을 해보자.
        # 다음칸이 이미 진행했던 곳이라면 카운트를 안해주는게 맞다 ( 어차피 종결지는 같을것이므로)

print(ans)
