import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
bridge = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    bridge[a].append((c,b))
    bridge[b].append((c,a))
start,end = map(int,input().split())


from typing import List,Optional
from collections import deque
def bfs(start : int) -> bool:
    visited = [0] * (n + 1)
    visited[start] = 1
    q = deque([start])
    while q:
        x = q.popleft()
        if x == end:
            return 1
        for cost,next_node in bridge[x]:
            if visited[next_node] or mid > cost : continue
            visited[next_node] = 1
            q.append(next_node)
    return 0

sn,en = 0,int(1e9)
ans = 0
while sn <= en:
    mid = (sn + en) // 2
    # 현재 최대 mid 만큼 옮길수있다면 mid 를 늘려보자
    if bfs(start):
        ans = mid
        sn = mid + 1
    else:
        en = mid - 1

print(ans)
