import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

a = []

for _ in range(n):
    a.append(list(map(int,input().split())))
# 모든사람이 한팀이 됐을때 최종점수
tot = 0
s = []
for i in range(n):
    temp = 0
    for j in range(n):
        temp += a[i][j]
    s.append(temp)
    tot += temp

ccc = combinations([i for i in range(n)],n // 2)
ans = int(1e10)
for cc in ccc:
    start = 0
    for i in cc:
        for j in cc:
            start += a[i][j]
    c_set = set(cc)
    link = 0
    for i in range(n):
        if i in c_set :continue
        for j in range(n):
            if j in c_set:continue
            link += a[i][j]
    ans = min(ans,abs(start - link))


print(ans)