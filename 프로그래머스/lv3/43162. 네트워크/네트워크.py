from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0]*n
    def bfs(x):
        q = deque([x])
        visited[x] = 1
        while q:
            x = q.popleft()
            for j in range(n):
                if visited[j] or computers[x][j] == 0 :continue
                visited[j] = 1
                q.append(j)
        return 1
    for i in range(n):
        if not visited[i] :
            answer += bfs(i)     
        
    return answer