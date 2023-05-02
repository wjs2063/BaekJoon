import sys
input = sys.stdin.readline


a,b = map(int,input().split())

# a * b < 0
if a * b < 0 :
    tot = 1 - (a / b)
    res = 12 / tot
    print(int(24 / res))
# a * b >= 0

else:
    tot = max(a/b,1) - min(a/b,1)
    res = 12 / tot
    print(int(24 / res))