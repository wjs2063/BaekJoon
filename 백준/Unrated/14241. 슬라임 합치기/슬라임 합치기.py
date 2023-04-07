import sys
from heapq import heappush,heappop,heapify
input = sys.stdin.readline


n = int(input())

s = list(map(int,input().split()))

heapify(s)
ans = 0
while len(s) > 1:
    x = heappop(s)
    y = heappop(s)
    ans += x * y
    heappush(s,x + y)
print(ans)