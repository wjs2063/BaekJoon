from collections import deque
def solution(maps):
    answer = []
    visited = [[0]*len(maps[0]) for _ in range(len(maps)) ]
    n = len(maps)
    m = len(maps[0])
    def bfs(i,j):
        q = deque([(i,j)])
        cnt = int(maps[i][j])
        visited[i][j] = 1
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        while q :
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] : continue
                if maps[nx][ny] == "X":continue
                visited[nx][ny] = 1
                cnt += int(maps[nx][ny])
                q.append((nx,ny))
        return cnt 
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != "X":
                answer.append(bfs(i,j))
    if len(answer) == 0:
        return [-1]
    else:
        answer.sort()
        return answer
    
    return answer