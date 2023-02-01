import sys
from collections import deque
input = sys.stdin.readline

f,s,g,u,d = map(int,input().split())

# f 는 총 층수
# s 는 시작층
# g 는 도착층
# u 는 위로 u칸
# d 는 아래로 d 칸

# bfs 로 풀자

def bfs(f,s,g,u,d):
    q = deque([(s,0)])
    visited = [0]*(f + 1)
    visited[s] = 1

    while q:
        x,cnt = q.popleft()
        if x == g :return cnt
        if x + u <= f and visited[x + u] == 0:
            visited[x + u] = 1
            q.append((x + u,cnt + 1))
        if 1 <= x - d and visited[x - d] == 0:
            visited[x - d] = 1
            q.append((x - d,cnt + 1))
    return - 1

res = bfs(f,s,g,u,d)

if res != -1:
    print(res)
else:
    print("use the stairs")