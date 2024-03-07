import sys
from heapq import heappush, heappop

si = sys.stdin.readline

n, m = map(int, si().split())

elec = list(map(int, si().split()))
h = []

for i, v in enumerate(elec):
    heappush(h, -v)

temp = []
ans = 0
while h:
    item = -heappop(h)
    temp.append(item)

    if len(temp) == m:
        first = temp[0]
        last = temp[-1]
        for i, v in enumerate(temp):
            if v - last > 0:
                heappush(h, -(v - last))
        ans += last
        temp = []

if temp :
    ans += temp[0]
print(ans)
