import sys
input = sys.stdin.readline

mw,mb = map(int,input().split())
tw,tb = map(int,input().split())
pw,pb = map(int,input().split())

a = min(mw,tb,pw)
b = min(mb,tw,pb)

if a < b :
    print(2 * a + 1)
elif a > b :
    print(2 * b + 1)
else:
    print(2*b)