import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
student = {}
for i in range(m):
    student[i] = list(map(int,input().split()))

"""
Goal
1 2 3 4 .. N 까지의 문제를 다풀줄아는 최소의 팀원을 모아야한다.
M = 10 일떄, 10C1 + 10C2 ... 10C10 := 2 ^10 이므로 완전탐색 충분히 가능 
combination 
"""
ans = float("inf")
# 뽑을사람 cnt 명
for cnt in range(1,m + 1):
    # 10명중 cnt 만큼 뽑고
    for cc in combinations([i for i in range(m)],cnt):
        temp = set()
        for c in cc :
            temp |= set(student[c][1:])
        # 모든문제가 다들어가있으면
        if len(temp) == n and cnt < ans :
            ans = cnt

print(ans if ans != float('inf') else -1)
