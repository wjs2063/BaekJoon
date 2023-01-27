import sys
from collections import deque
input = sys.stdin.readline

# 50m 가려면 맥주한병이 필요
# box 에는 맥주 20병이 넘을수없다
# 편의점을 나선 직후에도 50m 가기전에 맥주한병마시기
def bfs(s,r,cu):
    x,y = s
    rx,ry = r
    # beer 20개
    q = deque([(x,y,20)])
    visited = set()
    while q:
        x,y,b = q.popleft()
        # 현재위치 x,y 이고 맥주는 b 개있을떄
        # 현재 맥주 b 개로 갈수있는 위치인지판단
        # 만약 현재 beer 로 rock 에 갈수있다면?
        if abs(rx - x) + abs(ry - y) <= 50*b:
            return True
        #print(cu)
        #만약 다음 편의점에 가야한다면?
        for next_cu in cu:
            # 방문한 편의점이면 패스
            if next_cu in visited:continue
            # 다음 편의점에 갈수있다면
            nx,ny = next_cu
            if abs(x - nx) + abs(y - ny) <= 50*b:
                q.append((nx,ny,20))
                visited.add(next_cu)
    return False

t = int(input().strip())

for _ in range(t):
    n = int(input())
    cu = []
    beer = 20
    sx,sy = map(int,input().split())
    for _ in range(n):
        cu.append(tuple(map(int,input().split())))
    rx,ry = map(int,input().split())
    # beer 1개로 50 갈수있음
    if bfs((sx,sy),(rx,ry),cu):
        print("happy")
    else:
        print("sad")
