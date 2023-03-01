import sys
from collections import deque
si = sys.stdin.readline
N, K = map(int, si().split())
visited = [0 for _ in range(10**5 + 1)]
def bfs():
    q = deque()
    q.append([N, 0])
    visited[N] = 1
    while q:
        current, cnt = q.popleft()
        
        if current == K:
            print(cnt)
            return
        if current * 2 <= 10 ** 5 and visited[current * 2] == 0:
            q.appendleft([current * 2, cnt])
            visited[current *2] = 1 # 방문처리
        if 0 <= current - 1 <= 10 ** 5 and visited[current - 1] == 0:
            q.append([current- 1, cnt + 1])
            visited[current - 1] = 1 # 방문처리 
        
    
        if current + 1 <= 10 ** 5 and visited[current + 1] == 0:
            q.append([current + 1, cnt + 1])
            visited[current + 1] = 1 # 방문처리
    return
bfs()
