import sys
from collections import deque
input = sys.stdin.readline

k = int(input().strip())
# w 는 열
# h 는 행
w,h = map(int,input().split())
arr = []
for _ in range(h):
    arr.append(list(map(int,input().split())))


def bfs():
    q = deque([(0,0,k,0)])
    visited = set()
    visited.add((0,0,k))
    # 평범하게이동
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    #말처럼 이동
    hy = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
    while q:
        x,y,rest,cnt = q.popleft()
        if (x,y) == (h - 1,w - 1):
            return cnt
        # 평범하게 이동하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w or (nx,ny,rest) in visited :continue
            if arr[nx][ny] :continue
            visited.add((nx,ny,rest))
            q.append((nx,ny,rest,cnt + 1))
        # 말처럼 이동할수있는경우
        if rest > 0:
            for ds,dt in hy:
                ns = x + ds
                nt = y + dt
                if ns < 0 or ns >= h or nt < 0 or nt >= w or (ns,nt,rest - 1) in visited :continue
                if arr[ns][nt] :continue
                visited.add((ns,nt,rest - 1))
                q.append((ns,nt,rest - 1,cnt + 1))
    return -1

print(bfs())