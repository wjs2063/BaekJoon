import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

tot = 0
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            tot += 1

# 외곽을 어떻게판단하나?
# x,y 에 대해서 4방향 체크를 해서 0이면 외곽임

# q에 초기 좌표들 담고
# 초기좌표들을 돌면서 -> 외곽지역을 temp 에 담아

# 그리고 그 외곽지역을 일괄적으로 다 0 으로 만든다 그리고 계속 반복


# bfs 돌리는데 공기와 2개이상 마주친부분만 추가
ans = 0

def bfs(n,m):
    q  = deque([(0,0)])
    cnt = [[0]*m for _ in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    # 공기를 기준으로 bfs 돌려야한다
    cnt[0][0] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:continue
            # 공기주변에 치즈가있으면 카운트 추가
            if graph[x][y] == 0 and graph[nx][ny] == 1: cnt[nx][ny] += 1
            # 방문한적이없으면
            elif graph[nx][ny] == 0 and cnt[nx][ny] == 0:
                cnt[nx][ny] = 1
                q.append((nx,ny))
    return cnt







while tot:
    # 공기 2개이상 마주친 부분인 부분 추가
    cnt = bfs(n,m)
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if cnt[i][j] >= 2:
                graph[i][j] = 0
                tot -= 1
    ans += 1

print(ans)