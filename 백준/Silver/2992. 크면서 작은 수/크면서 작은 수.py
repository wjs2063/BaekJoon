import sys
from itertools import permutations
input = sys.stdin.readline


num = input().strip()

pp = list(permutations(list(num),len(num)))
num = int(num)
INF = int(1e10)
res = INF
for p in pp :
    temp = int("".join(p))
    if temp > num :
        res = min(res,temp)
if res == INF:
    print(0)
else:
    print(res)