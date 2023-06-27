import sys
from heapq import heappush,heappop
input = sys.stdin.readline

n = int(input())

h = []
# 길이가 n 짜리 힙
# -5000 ~ 5000 까지넣을떄 언제 빼고 언제 넣어야해
# 길이가 100짜리라면 제일 작은애보다 크다면 넣어야지
for _ in range(n):
    items = list(map(int,input().split()))
    for item in items :

        if (h and h[0] < item) or not h:
            heappush(h,item)
        #길이가 n 넘어가면 뺴
        if len(h) > n :
            heappop(h)

print(h[0])
