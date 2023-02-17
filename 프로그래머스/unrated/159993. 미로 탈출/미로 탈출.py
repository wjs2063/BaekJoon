from collections import deque
def bfs(maps,start,end):
    sx,sy = start
    ex,ey = end
    n,m = len(maps),len(maps[0])
    visited = [[0]*m for _ in range(n)]
    visited[sx][sy] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque([(sx,sy,0)])
    while q:
        x,y,cnt = q.popleft()
        if (x,y) == (ex,ey) :return cnt 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] :continue
            if maps[nx][ny] == "X":continue
            visited[nx][ny] = 1
            q.append((nx,ny,cnt + 1))
    return -1
    

def solution(maps):
    answer = 0
    # 레버로 가는 bfs 
    # 레버에서 출구로 가는 bfs
    start = 0
    lavv = 0
    out = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                start = (i,j)
            if maps[i][j] == "E":
                out = (i,j)
            if maps[i][j] == "L":
                lavv = (i,j)
    temp = bfs(maps,start,lavv)
    if temp == -1:
        return -1
    answer += temp
    temp = bfs(maps,lavv,out)
    if temp == -1:
        return -1
    return answer + temp