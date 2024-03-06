import sys
from collections import deque

si = sys.stdin.readline

w, h = map(int, si().split())
grid = []

for _ in range(h):
    grid.append(input().strip())
temp = []
for row in range(h):
    for col in range(w):
        if grid[row][col] == 'C':
            temp.append([row, col])

start, end = temp[0], temp[1]
"""
Goal 
거울의 최솟값, 
반대로 C 에서 시작해서 턴할떄마다 거울이있다고 생각 하자 
거리는 상관없이 turn 횟수의 최단거리가 중요하다 
"""


def in_grid(x, y, grid):
    n, m = len(grid), len(grid[0])
    if 0 <= x < n and 0 <= y < m: return 1
    return 0


def bfs(start, end, grid):
    n, m = len(grid), len(grid[0])
    sx, sy = start
    ex, ey = end
    q = deque([])
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    # 초기세팅
    INF = int(1e10)
    visited = [[ [INF] * 4 for _ in range(m) ] for _ in range(n)]
    visited[sx][sy][:4] = [0,0,0,0]
    # visited[x][y][a] := (x,y)를 a방향에서 왔을떄 소요한 거울의 개수
    for i in range(4):
        nx, ny = sx + dx[i], sy + dy[i]
        if not in_grid(nx, ny, grid): continue
        # 벽이면 패스
        if grid[nx][ny] == '*': continue
        # 이전 방향 기록
        q.append([nx, ny, i, 0])
        # 초기
        visited[nx][ny][i] = 0

    ans = INF

    while q:
        x, y, direction, cnt = q.popleft()
        if (x, y) == (ex, ey):
            if visited[x][y][direction] < ans:
                ans = visited[x][y][direction]
                continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not in_grid(nx, ny, grid): continue
            if grid[nx][ny] == '*': continue
            # 다음 칸에서 직진하거나 방향바꾸거나 , 다음칸으로 갈때 소요한거울의 개수가 현재보다 더작으면 안가도된다.
            if direction == i and (visited[nx][ny][i] > visited[x][y][direction]):
                q.append([nx,ny,i,cnt])
                visited[nx][ny][i] = visited[x][y][direction]
            if direction != i and (visited[nx][ny][i] > visited[x][y][direction] + 1):
                q.append([nx,ny,i,cnt + 1])
                visited[nx][ny][i] = visited[x][y][direction] + 1
    return ans


print(bfs(start, end, grid))
