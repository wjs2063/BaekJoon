# 다익스트라 알고리즘
# a 정점에서 갈수있는 다른 모든 노드까지의 최단거리


# BOJ 1753 최단경로 문제 예시
import sys
from heapq import heappush, heappop

"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""

input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b, c))
    # u 에서 v 로 가는 가중치 w
INF = int(1e10)
def dijkstra(start):
    h = []
    distance = [INF for _ in range(V + 1)]
    # distance[x] := start 에서 x 까지의 최단 거리
    distance[start] = 0 # start 에서 start 는 0 이다,
    heappush(h,(0,start))
    # heap 을 쓰는 이유는 현재기준 제일 짧은거리를 가져오겠다는 의미
    while h :
        dist,now = heappop(h)
        if distance[now] < dist:continue # start에서 now 까지 거리가 현재 거리보다 작으면 그냥 패스
        for adj_node,c in graph[now]:
            # 현재 비용 + adj_node 로 가는 비용 := cost
            cost = dist + c
            if cost < distance[adj_node]: # 최단거리 일지에 적혀있는 start -> adj_node 까지가는 거리 랑 비교하자
                # now 를 거쳐 adj_node 를 가는게 더 저렴하다면 갱신해주는게좋겠지?
                distance[adj_node] = cost
                heappush(h,(cost,adj_node))
    return distance
# 다익스트라 돌리기
distance = dijkstra(start)
for i in range(1,V + 1):
    if distance[i] == INF :
        print("INF")
    else:
        print(distance[i])

