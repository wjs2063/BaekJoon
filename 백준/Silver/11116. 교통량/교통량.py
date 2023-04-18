import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    l = Counter(list(map(int,input().split())))
    r = Counter(list(map(int,input().split())))
    ans = 0
    for x in l :
        if x + 500 in l and x + 1000 in r and x + 1500 in r:
            ans += 1
    print(ans)