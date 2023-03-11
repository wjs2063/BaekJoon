from collections import deque
def solution(maps):
    answer = 0
    def bfs():
        q = deque([(0,0)])
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        n,m = len(maps),len(maps[0])
        vis = [[0]*m for _ in range(n)]
        vis[0][0] = 1
        while q:
            x,y = q.popleft()
            if (x,y) == (n - 1,m - 1):
                return vis[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and maps[nx][ny] == 1:
                    vis[nx][ny] = vis[x][y] + 1
                    q.append((nx,ny))
        return -1
            
            
            
    return bfs()