import sys
from collections import defaultdict
from heapq import heappush, heappop

si = sys.stdin.readline

n, m = map(int, si().strip().split())

graph = defaultdict(list)

for i in range(m):
    period = i
    a, b = map(int, si().strip().split())
    graph[a].append((b, period))
    graph[b].append((a, period))


# graph[x] := x 꼭지점에서 갈수있는 지점의 번호와, 파란불 주기

# 1 번에서 -> 갈수있는 모든 지점


def dijkstra(start: int, graph: dict, n: int, m: int):
    INF = int(1e11)

    distance = [INF] * (n + 1)
    distance[start] = 0

    h = [(0, start)]

    while h:
        # node 와 time= 건넌데 소요된 시간
        current_time, node = heappop(h)
        #print(node,distance)
        # find 연결된지점
        for next_node, next_node_period in graph[node]:
            current_time_mod = current_time % m

            if current_time_mod > next_node_period:
                wait_time = next_node_period + m - current_time_mod
            else:
                wait_time = abs(current_time_mod - next_node_period)
            #  현재 시간에서 - 기다려야하는 시간 + 건너는 시간
            next_current_time = current_time + wait_time + 1
            if next_current_time >= distance[next_node]: continue
            distance[next_node] = next_current_time
            heappush(h, (distance[next_node], next_node))
    return distance[n]

print(dijkstra(1, graph, n, m))
