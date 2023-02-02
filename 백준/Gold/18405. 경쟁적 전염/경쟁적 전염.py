import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
arr = []
virus = [[] for _ in range(k + 1)]
for i in range(n):
    arr.append(list(map(int,input().split())))
    for j in range(n):
        if arr[i][j] != 0:
            virus[arr[i][j]].append((i,j))

s,x,y = map(int,input().split())

def bfs(s,u,v):
    q = deque([])
    # virus 번호 순서대로 넣자
    for i in range(1,k + 1):
        for j in range(len(virus[i])):
            q.append(virus[i][j] + (0,))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        #바이러스 번호순서대로 들어가있으니
        x,y,time = q.popleft()
        # s 보다 커지면 볼필요가없으므로 다패스
        if time + 1 > s:continue
        if time == s and (x,y) == (u - 1,v - 1):
            return arr[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위벗어나면 패스해주고
            if nx < 0 or nx >= n or ny < 0 or ny >= n:continue
            # 들어있으면 패스
            if arr[nx][ny] != 0 :continue
            # x,y에 들어있는값을 넣기
            arr[nx][ny] = arr[x][y]
            q.append((nx,ny,time + 1))
    return arr[u - 1][v - 1]
ans = bfs(s,x,y)

if ans != 0:
    print(ans)
else:
    print(0)
