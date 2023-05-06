import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    res = 0
    for _ in range(n):
        a,b,c = map(int,input().split())
        arr.append(sorted([a,b,c],reverse = True))
        if arr[-1][0] > 0 :
            res += arr[-1][0]
    print(res)