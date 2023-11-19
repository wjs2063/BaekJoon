import sys
from collections import deque

n = int(input())

grid = []

for _ in range(n):
    grid.append(list(map(int,input().split())))

dirs = [(0,1),(1,0)]

def solution(n,grid):
    q = deque([(0,0)])
    vis = set()
    vis.add((0,0))
    while q:
        r, c = q.popleft()
        jump = grid[r][c]
        for idx,(dr,dc) in enumerate(dirs):
            nr,nc = r + dr * jump, c + dc * jump

            if not (0 <= nr < n and 0 <= nc < n):continue
            if (nr,nc) in vis:continue
            if grid[nr][nc] == -1:
                return "HaruHaru"
            vis.add((nr,nc))
            q.append((nr,nc))
    return "Hing"

print(solution(n,grid))