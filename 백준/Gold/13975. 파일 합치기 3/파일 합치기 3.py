import sys
input = sys.stdin.readline
import heapq

t = int(input())

for _ in range(t):
    n = int(input())
    files = list(map(int,input().split()))
    # 작은 애들끼리만 계속 합치자
    heapq.heapify(files)
    answer = 0
    # 가장 작은 애들끼리 합치는게 제일 효율적이다
    # heapq 의 insert 는 O(logN) 이므로 
    # 몇번반복할까? 2개가 1개 되고 3개가 2개 되고 -> N - 1번반복하겠네.
    # O(NlogN) 에 풀수있다.
    while len(files) != 1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        answer += a + b
        heapq.heappush(files,a + b)
    # 1개남았을때 종료 
    print(answer)
