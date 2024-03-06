import sys
from collections import deque

si = sys.stdin.readline

n, m = map(int, si().split())

grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]


def bfs(grid, visited, r, c):
    q = deque([(r, c)])
    memo = set()
    memo.add((r, c))
    n, m = len(grid), len(grid[0])
    same_level_queue = deque([(r, c)])
    # q 에 모두다 담아보자,
    while q:
        x, y = q.popleft()
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),(x - 1,y - 1),(x - 1,y + 1),(x + 1,y - 1),(x + 1,y + 1)]:
            if not (0 <= nx < n and 0 <= ny < m): continue
            if grid[x][y] != grid[nx][ny]: continue
            if (nx, ny) in memo: continue
            visited[nx][ny] = 1
            memo.add((nx, ny))
            q.append((nx, ny))
            same_level_queue.append((nx, ny))
    while same_level_queue:
        x, y = same_level_queue.popleft()
        # 외각지역이 현재보다 아래인지 판단
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),(x - 1,y - 1),(x - 1,y + 1),(x + 1,y - 1),(x + 1,y + 1)]:
            if not (0 <= nx < n and 0 <= ny < m): continue
            if (nx, ny)  in memo: continue
            if grid[nx][ny] >= grid[x][y]: return 0
    return 1


ans = 0
for r in range(n):
    for c in range(m):
        # 현재 v 값
        if visited[r][c]: continue
        flag = bfs(grid,visited,r,c)
        if flag:
            ans += 1
print(ans)
