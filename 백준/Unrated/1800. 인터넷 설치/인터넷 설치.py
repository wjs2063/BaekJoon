import sys
from collections import defaultdict
from heapq import heappush,heappop
input = sys.stdin.readline


n,p,k = map(int,input().split())

grp = defaultdict(list)


for _ in range(p):
    a,b,c = map(int,input().split())
    grp[a].append((b,c))
    grp[b].append((a,c))

def dijkstra(mid):
    INF = int(1e10)
    distance = [INF]*(n + 1)
    distance[1] = 0
    # distance[n] : 1 ~ n 까지 오는데 사용한 케이블 개수
    # 내가 낼 금액이 mid 이니까 mid 보다 크면 공짜케이블에 추가해
    q = [(0,1)]

    while q:
        cnt,root = heappop(q)
        if distance[root] < cnt:continue
        for nn,nn_cost in grp[root]:
            # 공짜케이블로 넘겨
            c = cnt
            if nn_cost > mid:
                c += 1
            if distance[nn] <= c:continue
            distance[nn] = c
            heappush(q,(c,nn))
    return distance[n] <= k


sn,en = 0,int(1e6)
ans = -1

while sn <= en :
    mid = (sn + en) // 2

    ff = dijkstra(mid)

    # 공짜 케이블수가 적다는건 그만큼 낼돈이 많다는 뜻
    if ff :
        ans = mid
        en = mid - 1
    else:
        sn = mid + 1
print(ans)


