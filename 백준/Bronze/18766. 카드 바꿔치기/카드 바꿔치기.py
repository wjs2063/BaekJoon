import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = Counter(input().split())
    b = Counter(input().split())
    f = 0
    for key in a :
        if a[key] != b[key]:
            f = 1
            break
    if f :
        print("CHEATER")
    else:
        print("NOT CHEATER")