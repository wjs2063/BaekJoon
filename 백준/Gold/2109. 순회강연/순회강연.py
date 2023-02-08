import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())

arr = []

for _ in range(n):
    p,d = map(int,input().split())
    arr.append((d,p))

arr.sort()


h = []
# h의길이는 현재 지난날짜 -> 길이가 4이면 4일이다
for a,b in arr:
    # heap 에는 작은값만 들어감
    heapq.heappush(h,b)

    if len(h) > a :
        heapq.heappop(h)

print(sum(h))