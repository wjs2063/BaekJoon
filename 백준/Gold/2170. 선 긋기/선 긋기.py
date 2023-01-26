import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())

h = []

for _ in range(n):
    a,b = map(int,input().split())
    heapq.heappush(h,(a,b))
# 겹치는 부분을 제외 시켜주어야한다.
ans = 0
while h:
    # left <= x <= right 처럼 저장되어있는데
    sn,en = heapq.heappop(h)
    #겹친다면 계속 저장해주고
    while h and h[0][0] <= en:
        x,y = heapq.heappop(h)
        en = max(en,y)
    # 최종적으로
    ans += en - sn
print(ans)