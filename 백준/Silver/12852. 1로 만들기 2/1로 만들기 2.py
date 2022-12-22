import sys
from _collections import defaultdict,deque
input = sys.stdin.readline
n = int(input().strip())

def bfs(n):
    visited = [False] * (n + 1)
    visited[n] = True
    cnt = 0
    if n == 1:
        return 0, {1}
    path = set([n])
    q = deque([(n,0,path)])
    while q:
        num, distance, pt = q.popleft()
        if num == 1:
            return distance,pt
        # 3으로 나누어떨어질때
        if num % 3 == 0:
            if not visited[num // 3] :
                visited[num % 3] = True
                q.append((num // 3,distance + 1,pt | {num // 3}))
        if num % 2 == 0:
            if not visited[num // 2]:
                visited[num // 2] = True
                q.append((num // 2 ,distance + 1, pt | {num // 2}))
        if not visited[num - 1]:
            visited[num - 1] = True
            q.append((num - 1,distance + 1,pt | {num - 1}))

        # 2로나 나누어 떨어질떄
        # 1로 뺼때 중 제일 빨리도착하는것
    return
x,y = bfs(n)

print(x)
print(*sorted(y,reverse = True))
