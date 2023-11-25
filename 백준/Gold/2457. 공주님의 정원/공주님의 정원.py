"""
N개의 꽃
1. 같은해에 피어서 같은해에 진다.
2. 4,6,9,11 -> 30일
   1,3,5,7,8,10,12 -> 31일
   2 -> 28일
3. 3월 1 ~ 11월 30일까지 1개이상의 꽃이 피어있어야함
4. 정원에 심는 꽃들의 수를 가능한 적게.
"""
import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush
from collections import deque

input = sys.stdin.readline

day = defaultdict(int)
for m in [4, 6, 9, 11]:
    day[m] = 30
for m in [1, 3, 5, 7, 8, 10, 12]:
    day[m] = 31
day[2] = 28
prefix = defaultdict(int)
year = [i + 1 for i in range(1, 12)]

for m in year:
    prefix[m] += prefix[m - 1] + day[m - 1]
# prefix[a] := a월 1일 이전까지의 누적일수
n = int(input())

lines = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    start = prefix[sm] + sd
    end = prefix[em] + ed - 1
    # lines -> start 일부터 end일까지 펴있는 꽃
    lines.append([start, end])
# 3월 1일부터 , 11월 30일까지
sn = prefix[3] + 1
en = prefix[12] # 11월 30일

# sn <= x <= en 까지 모두 덮는데 최소의 선분개수를 구하는 문제와 똑같다.

start = sn
heapify(lines)
res = 0
last = 0
# print(start)
while lines:
    # lines-> [start,end] 인데
    # 우리는 sn <= LINE < en 을 다덮을수있는 선분의 최소의 개수를 구하고싶은거다.
    temp = start
    # lines 를 돌면서 현재 start 보다 이전에 핀 꽃들을 검사하면서 마지막 지는날이 제일 긴것들을 체크한다.
    # lines a <= 피어있는날짜 <= b , a일부터 b일까지는 피어있다
    flag = 1
    while lines and lines[0][0] <= start:
        s, e = heappop(lines)
        temp = max(temp, e)
        flag = 0
    # lines[x] x번쨰원소가 -> 꽃이 a일부터 b일까지 피어있다는 의미,
    # 변함이없으면 더이상 진행될게없다는 의미
    if flag:break
    res += 1
    last = temp 
    start = temp + 1
    if temp >= en:
        start = temp
        break
    
    # 최종날짜가 끝났으면
if last < en:
    print(0)
else:
    print(res)