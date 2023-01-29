import sys
from itertools import permutations,product

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    ans = []
    # oprand 는 n - 1개 이다
    # + , - , "" 로 모든것을 해결
    # - 는 무조건 포함
    x = [str(i) for i in range(1,n + 1)]
    ppp = product(["+","-"," "],repeat = n - 1)
    for pp in ppp:
        if "-" not in pp :continue
        ss = ""
        ss += x[0]
        temp = ""
        temp += x[0]
        i = 1
        for p in pp:
            ss += p
            if p != " ":
                temp += p
            ss += x[i]
            temp += x[i]
            i += 1
        if eval(temp) == 0:
            ans.append(ss)
    for x in sorted(ans):
        print(x)
    print()