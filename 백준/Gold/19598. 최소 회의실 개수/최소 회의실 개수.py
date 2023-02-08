import sys
import heapq
input = sys.stdin.readline

n = int(input())

sc = []

for _ in range(n):
    a,b = map(int,input().split())
    sc.append((a,b))
sc.sort(key = lambda x:(x[0],-x[1]))

h = []
ans = 0
for sn,en in sc:
    # heap 에는 종료시점만 넣고
    # 시작점보다 먼저 끝나는 경우는 다 컷
    if h and h[0] <= sn:
        heapq.heappop(h)
    heapq.heappush(h,en)
    ans = max(ans,len(h))
print(ans)