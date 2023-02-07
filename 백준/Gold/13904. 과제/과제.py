import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())

# 남은 일수 , 과제점수
arr = []

for _ in range(n):
    a,b = map(int,input().split())
    heapq.heappush(arr,(a,b))
# 마감기한이 제일 빠른순으로 일단 처리해보자

h = []

while arr:
    x,y = heapq.heappop(arr)
    # 과제점수를 추가하자
    # h의 길이 는 진행일수이다
    heapq.heappush(h,y)

    if x < len(h):
        heapq.heappop(h)
print(sum(h))
