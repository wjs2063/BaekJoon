import sys
from _collections import defaultdict,deque
input = sys.stdin.readline

n,m = map(int,input().split())

graph = defaultdict(list)

for _ in range(n - 1):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
for x in graph:
    graph[x].sort()
# bfs 로 두노드 간의 거리
# n 10^3 이고 m 도 10 ^ 3이므로 시복 충분히가능

def bfs(n,start,end):
    global graph
    q = deque([(start,0)])
    visited = set()
    while q:
        node,dist = q.popleft()
        if node == end:
            return dist
        for d,next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                q.append((next_node,dist + d))
    return 0

for _ in range(m):
    start,end = map(int,input().split())
    print(bfs(n,start,end))