import sys
from collections import defaultdict,deque
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())
s,e = map(int,input().split())

graph = defaultdict(list)
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))



# a -> b -> c -> 목적지
# 그래프가 주어지면 일단 가기만 하면 된다.
# 뭐가됐던 묶어주기만 하면됨
# s -> e ? 다익인데 큰놈들로
# 7 5 3 보다
# 7 6 6 5

def dijkstra(s,e):
    #최대한 큰애들로
    INF = int(1e7)
    distance = [0]*(n + 1)
    res = INF
    q = []
    heapq.heappush(q,(-INF,s))
    # 중량이 큰것
    # distance[x] := x번째노드를갈때 최대중량
    while q:
        dist,node = heapq.heappop(q)
        # 양수로
        dist = -dist
        # 현재 node 로 갈수있는 중량보다 작으면 패스
        if distance[node] > dist:continue
        # 현재 node 와 연결되어있는 노드중에서
        for cost,next_node in graph[node]:
            # 현재 값과 다음 노드값중 작은값으로
            tt = min(cost,dist)
            if distance[next_node] >= tt:continue
            distance[next_node] = tt
            heapq.heappush(q,(-tt,next_node))
    print(distance[e])
dijkstra(s,e)

