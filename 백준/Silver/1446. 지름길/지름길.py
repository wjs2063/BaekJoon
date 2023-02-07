import sys
import heapq

input = sys.stdin.readline

n,d = map(int,input().split())

# 지름길을 이용하지않고 가는경우
distance = [i for i in range(d + 1)]
fast = []

for _ in range(n):
    a,b,c = map(int,input().split())
    fast.append((a,b,c))

h = []

heapq.heappush(h,(0,0))

# distance[x] -> x 까지 오는데 걸리는 최단시간

while h:
    # 현재 위치 pos, 시간 cost
    cost, pos = heapq.heappop(h)
    if cost + d - pos < distance[d]:
        distance[d] = cost + d - pos
    if distance[pos] < cost:continue
    # 현재지점에서 바로 d까지 가는방법

    for x,y,c in fast:
        # 지름길의 시작지점이 현재위치보다 낮으면 패스
        if x < pos : continue
        # 역주행 불가능하니까 패스
        if y > d:continue
        # 위치는 pos - 지름길시작지점(x) - 지름길 도착지점(y) pos <= x <= y , c 는 비용
        # 현재지점에서 조금 더 가서 지름길을 이용하는경우가있다.
        if x - pos + c < distance[y]:
            distance[y] = cost + x - pos + c
            heapq.heappush(h,(cost + x - pos + c,y))
print(distance[d])


