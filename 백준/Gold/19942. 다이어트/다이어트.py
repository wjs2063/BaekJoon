import sys
from itertools import combinations


input = sys.stdin.readline


n = int(input())
table = []

standard = list(map(int,input().split()))

for _ in range(n):
    table.append(list(map(int,input().split())))

def solution(n,standard,table):
    res = []
    mp, mf, ms, mv = standard
    idx_list = [i for i in range(n)]
    for k in range(1,n + 1):
        cc = combinations(idx_list, k)
        for c in cc :
            money = 0
            tot_p,tot_f,tot_s,tot_v = 0, 0, 0, 0
            for idx in c :
                p, f, s, v, m = table[idx]
                tot_p += p
                tot_f += f
                tot_s += s
                tot_v += v
                money += m
            if tot_p >= mp and tot_f >= mf and tot_s >= ms and tot_v >= mv :
                res.append([money] + list(c))
    res.sort()
    if not res :
        print(-1)
        return
    min_res = res[0]
    print(min_res[0])
    r = [i + 1 for i in min_res[1:]]
    print(*r)
solution(n,standard,table)





