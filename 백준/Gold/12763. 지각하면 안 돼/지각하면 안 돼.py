import sys
import heapq
si = sys.stdin.readline
n = int(si().strip())

T,m = map(int,si().split())

l = int(si())

arr = [[] for _ in range(n + 1)]

for _ in range(l):
    a,b,time,cost = map(int,si().split())
    arr[a].append((b,time,cost))
    arr[b].append((a,time,cost))
INF = int(1e10)
distance = [[INF]*(T + 1) for _ in range(n + 1)]
# distance[node][x] : node 까지오는데 걸리는 x만큼의 시간을 썻을때 드는 비용
distance[1][1] = 0
h = []
heapq.heappush(h,(0,(1,0)))
ans = INF
while h:
    # 현재 노드까지오는데 드는 시간,현재노드,돈
    time,(node,cost) = heapq.heappop(h)
    # T 시간내로 갈수있는 후보들만 체크
    if distance[node][time] < cost  : continue
    for next_node,t,money in arr[node]:
        # 주어진 조건내로 갈수있다면
        if time + t <= T and cost + money <= m:
            if cost + money < distance[next_node][time + t]:
                distance[next_node][time + t] = cost + money
                heapq.heappush(h,(time + t,(next_node,cost + money)))

ans = INF
for i in range(1,T + 1):
    ans = min(ans,distance[n][i])
if ans != INF:
    print(ans)
else:
    print(-1)



