import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())

line = []

for _ in range(n):
    sn,en = map(int,input().split())
    heapq.heappush(line,(sn,en))
# 겹치는거 담을 변수 temp
temp = []
answer = 0
# O(NlogN)
while line:
    #sn en 을 한개씩 빼면서
    sn,en = heapq.heappop(line)
    # 현재 좌표보다 더 왼쪽에있는거면 뺴자
    while temp and temp[0] <= sn :
        heapq.heappop(temp)
    # 끝점을 넣어주자
    heapq.heappush(temp,en)
    answer = max(answer,len(temp))
print(answer)