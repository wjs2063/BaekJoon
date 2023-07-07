import sys
from heapq import heappush,heappop,heapify
input = sys.stdin.readline

n = int(input())

lines = []
for _ in range(n):
    a,b = map(int,input().split())
    lines.append([a,-b])

heapify(lines)

L,P = map(int,input().split())

start = 0
fuel = [-P]
ans = -1
while start < L :
    if not fuel :
        ans = -1
        break
    P = -heappop(fuel)
    ans += 1
    # 현재 연료로 갈수있는 주유소의 연료량을 다 넣어준다
    while lines and lines[0][0] <= start + P :
        x,y = heappop(lines)
        heappush(fuel,y)
    # 위치 이동시키고
    start += P

print(ans)