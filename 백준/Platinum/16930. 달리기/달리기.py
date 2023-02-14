import sys
from collections import deque
input = sys.stdin.readline


n,m,k = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(input().strip())

x1,y1,x2,y2 = map(int,input().split())
#시작점이 1,1 부터니  -1 을 해주자

x1,y1,x2,y2 = x1 - 1,y1 - 1,x2 -1 ,y2 - 1


# 세로,가로로 갈수있는지 여부를 판단하는 배열을 생성해주면 될거같은데?
dp = [[0]*m for _ in range(n)]
# dp[x][y] -> dp[x - 1][y] -> (x - 1,y ) 에서 (x,y) 로 갈수있나? dp[x][y] -> dp[x - 3][y] -> (x - 3,y) ,ㅇ서 x,y갈수있나?
# dp[i][j] 로 먼저 bfs 돌린후에 -> abs(dp[i + k][j] - dp[i][j]) 값이 k 라면 직선으로 갈수있다는 뜻 아닐까?
visited = [[0]*m for _ in range(n)]

def bfs1(sx,sy,visited):
    q = deque([(sx,sy)])
    visited[sx][sy] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 밤위,벽,방문한곳이면 패스
            if nx < 0 or nx >= n or ny < 0 or ny >= m or arr[nx][ny] == "#" or visited[nx][ny] :continue
            q.append((nx,ny))
            visited[nx][ny] = 1
            dp[nx][ny] = dp[x][y] + 1
#거리먼저 갱신후에

for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == ".":
            bfs1(i,j,visited)


def bfs():
    q = deque([(x1,y1,0)])
    visited = [[0]*m for _ in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        a,b,cnt = q.popleft()
        #도착지점에 먼저 도착하면 return
        if (a,b) == (x2,y2):
            return cnt
        for i in range(4):
            for d in range(1,k + 1):
                # 예를들어 (a,b) 에서 -> (a + d,b) 까지 간다고 해보자 그사이에 장애물이없어야 갈수있다
                nx = a + dx[i] * d
                ny = b + dy[i] * d
                # 범위,방문 패스
                if nx < 0 or nx >= n or ny < 0 or ny >= m :continue
                # 벽 패스
                if visited[nx][ny] and abs(dp[nx][ny] - dp[a][b]) != d:continue
                if arr[nx][ny] == "#":break
                # abs(dp[nx][ny] - dp[a][b) 가 d 가 아니면 직선으로 갈수없다는소리다.
                if not visited[nx][ny]:
                    q.append((nx,ny,cnt + 1))
                    visited[nx][ny] = visited[a][b] + 1
                elif visited[nx][ny] == visited[a][b] + 1:continue
                else:
                    break
    return -1

print(bfs())