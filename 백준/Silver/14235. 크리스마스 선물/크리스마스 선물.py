import sys
from heapq import heappush,heappop
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    si = list(map(int,input().split()))
    if si[0] == 0:
        if h :
            print(-heappop(h))
        else:
            print(-1)
    for item in si[1:] :
        heappush(h,-item)
