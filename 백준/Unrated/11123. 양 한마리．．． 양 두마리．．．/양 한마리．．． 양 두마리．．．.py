from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def bfs(x,y,seen):
    seen.add((x,y))
    q = deque([(x,y)])

    while q:
        x,y = q.popleft()
        for nx,ny in [(x + 1,y),(x - 1,y),(x,y + 1),(x,y - 1)]:
            if not (0 <= nx < h and 0 <= ny < w):continue
            if (nx,ny) in seen or grid[nx][ny] == '.':continue
            seen.add((nx,ny))
            q.append((nx,ny))
    return 1

for _ in range(t):
    h,w = map(int,input().split())
    grid = []
    seen = set()
    for _ in range(h):
        grid.append(input().strip())
    ans = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#" and (i,j) not in seen:
                ans += bfs(i,j,seen)
    print(ans)
