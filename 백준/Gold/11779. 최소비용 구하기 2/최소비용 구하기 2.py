import sys
from _collections import defaultdict,deque
import heapq
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
graph = [[] for _ in range(n + 1)]

#문제에서 도시번호가 1 ~ n 이라는 말이있나?
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))

start,end = map(int,input().split())

# 모든 간선들에 대해 E 번 -> heap -> log E
# O(ElogE)
def dijkstra(start):
    INF = int(1e10)
    q = []
    heapq.heappush(q,(0,start,f"{start}"))
    distance = [[INF,""]]*(n + 1)
    distance[start] = (0,f"{start}")
    while q:
        # vertex 까지오는데 비용 dist, 경로 path
        dist,vertex,path = heapq.heappop(q)
        if dist > distance[vertex][0]:continue
        # 현재 vertex 와 연결된  노드로가는 비용과  next_node 번호
        for cost,next_node in graph[vertex]:
            # 현재까지 오는데 드는 비용 + 다음까지가는데 비용이 -> next_node 까지가는데 걸리는 비용보다 적다면 갱신
            if dist + cost < distance[next_node][0]:
                distance[next_node] = (dist + cost,path + f" {next_node}")
                heapq.heappush(q,(distance[next_node][0],next_node,path + f" {next_node}"))
    return distance

temp = dijkstra(start)

print(temp[end][0])
x = temp[end][1].split()
print(len(x))
print(*x)
