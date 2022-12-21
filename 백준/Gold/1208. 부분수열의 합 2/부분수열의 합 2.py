import sys
input = sys.stdin.readline
from collections import defaultdict
from itertools import combinations
n,s = map(int,input().split())
seq = list(map(int,input().split()))

sq1,sq2 = seq[:n//2],seq[n//2:]

dt1 = defaultdict(int)
dt2 = defaultdict(int)
for i in range(1,len(sq1) + 1):
    cc = combinations(sq1,i)
    for c in cc:
        dt1[sum(c)] += 1

for i in range(1,len(sq2) + 1):
    cc = combinations(sq2,i)
    for c in cc:
        dt2[sum(c)] += 1
# 합이 s? s 와 0 의 조합일수도 or s 만일수도
answer = dt1[s] + dt2[s]

for k in dt1:
    answer += dt1[k]*dt2[s - k]
print(answer)

