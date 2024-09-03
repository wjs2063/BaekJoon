import heapq
import sys
from _collections import defaultdict

si = sys.stdin.readline

n, m = map(int, si().strip().split())

farm = defaultdict(list)
cost = []
for _ in range(m):
    a, b, c = map(int, si().strip().split())
    # cost.append((c, a, b))
    farm[a].append((b, c))
    farm[b].append((a, c))
# cost.sort(key=lambda x: x[0])
start = 1


# 1 -> N 으로 가는 최소비용

# kruscal or dijkstra

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# def union_parent(parent, x, y):
#     a = find_parent(parent, x)
#     b = find_parent(parent, y)
#     parent[a] = b
#
#
# parent = [i for i in range(n + 1)]

def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    INF = int(1e10)
    distance = [INF] * (n + 1)
    distance[start] = 0
    while h:
        cost,node = heapq.heappop(h)
        if distance[node] < cost: continue
        for next_node, weight in farm[node]:
            if distance[next_node] > cost + weight:
                distance[next_node] = cost + weight
                heapq.heappush(h, (cost + weight, next_node))
    return distance[n]

print(dijkstra(start))