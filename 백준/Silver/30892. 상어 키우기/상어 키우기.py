import sys
from heapq import heappush, heappop, heapify

si = sys.stdin.readline

n, k, t = map(int, si().split())
A = list(map(int, si().split()))

heapify(A)
cnt = 0
can_eat = []
# 잡아먹을수있는것들중 제일 큰놈부터 잡아먹자

while cnt < k:
    if not can_eat and A and A[0] >= t:
        break

    while A and A[0] < t:
        shark = heappop(A)
        heappush(can_eat, -shark)
    if can_eat:
        x = -heappop(can_eat)
        cnt += 1
        t += x
print(t)
