import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input().strip())

conf = []

for _ in range(n):
    start,end,p = map(int,input().split())
    conf.append((start,end,p))
conf.sort()
answer = 0

def check(cc):
    #사람수
    temp = 0
    # 시작시간
    t = 0
    for sn,en,p in cc:
        if t <= sn:
            temp += p
            t = en
        else:
            return False,temp
    return True,temp


for i in range(1,n + 1):
    ccc = combinations(conf,i)
    for cc in ccc:
        flag,temp = check(cc)
        if flag:
            answer = max(answer,temp)
print(answer)
