import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
# 문제 해결 포인트
# 지금 좌표에서 인접한 곳이지만  나중에 저 멀리가서 불을 켤수있는경우는 어떻게 처리할것인가? 이게포인트다.
# 즉 1,1 에서 1,2 를 살펴볼떄 지금당장은 켜져있지않았지만 나중에 5,5 에가서 1,2를 켤수있는경우가있다
# 이부분을 해결해주면 풀릴수있는 문제다

n,m = map(int,input().split())
arr = defaultdict(list)
for _ in range(m):
    x,y,a,b = map(int,input().split())
    arr[(x,y)].append((a,b))
# 불이 켜져있는지 확인하는 visited
light = [[0]*(n + 2) for _ in range(n + 2)]
visited = [[0]*(n + 2) for _ in range(n + 2)]

# 불은 켤수있으나 가지못하는점
# 불 켤수있고 갈수도있는점
def bfs():
    q = deque([(1,1)])
    n = len(visited)
    # 현재지점 불은 켜져있어양함
    light[1][1] = 1
    visited[1][1] = 1
    cnt = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x,y = q.popleft()
        # 불을 켤수있으면 다 켜자
        # x,y 에서 켤수있는 지점은 다 켜자
        for rx,ry in arr[(x,y)]:
            if light[rx][ry] :continue
            light[rx][ry] = 1
            cnt += 1
            for i in range(4):
                nx = rx + dx[i]
                ny = ry + dy[i]
                if nx <= 0 or nx > n or ny <= 0 or ny > n :continue
                # 방문한적이있으면 다시 불을 켰으므로 다시확인
                if visited[nx][ny]:
                    q.append((nx,ny))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 현재 갈수있는 지점에서 다 가서 불일단 다켜
            if nx <= 0 or nx > n or ny <= 0 or ny > n or light[nx][ny] == 0 or visited[nx][ny] :continue
            visited[nx][ny] = 1
            q.append((nx,ny))
    return cnt
print(bfs())

