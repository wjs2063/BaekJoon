import sys
import heapq
from _collections import defaultdict
input = sys.stdin.readline

n,m = map(int,input().split())

view = list(map(int,input().split()))

graph = defaultdict(list)

for _ in range(m):
    a,b,t = map(int,input().split())
    graph[a].append((t,b))
    graph[b].append((t,a))


def dijkstra(start,n):
    q = []
    INF = int(1e10)
    distance = [INF]*n
    # 출발지점이 보이는곳이면 return
    if view[start] == 1:return distance[n - 1]
    # 시작지점은 0
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        dist,node = heapq.heappop(q)
        if dist > distance[node]:continue
        # 현재 node 와 연결된 다음 노드를 봅시다
        for cost,next_node in graph[node]:
            # n - 1번쨰노드가아니고 시야에 보이는곳 이라면
            if view[next_node] == 1 and next_node != n - 1 : continue
            # 더 짧은 비용으로 갈수있으면
            if dist + cost < distance[next_node]:
                distance[next_node] = dist + cost
                heapq.heappush(q,(distance[next_node],next_node))
    return distance[n - 1]

ans = dijkstra(0,n)
if  ans == int(1e10):
    print(-1)
else:
    print(ans)

