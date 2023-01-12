import sys
import heapq
input = sys.stdin.readline

info = []

n = int(input().strip())

for i in range(n):
    deadline,cup_noodle = map(int,input().split())
    heapq.heappush(info,(deadline,cup_noodle ,i + 1))
# deadline 이 짧은거부터 해결은 해야한다.
cup = []
while info:
    dead_line,c,num = heapq.heappop(info)
    heapq.heappush(cup,c)
    # 문제푸는데 걸리는 시간이 1이라는 소리가 결국 푼 문제의 개수 == 걸린시간이라는 소리다
    # 현재 시점의 dead_line 을 기점으로 만약 풀수있는 문제(걸린시간)(cup의 길이) 이 deadline 이 넘어가잖아?
    # 그러면 제일 효율 이안좋은애 를 뺴봐
    if dead_line < len(cup):
        heapq.heappop(cup)
print(sum(cup))
