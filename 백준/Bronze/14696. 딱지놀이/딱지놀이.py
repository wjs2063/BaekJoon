import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a = a[1:]
    b = b[1:]
    ca = Counter(a)
    cb = Counter(b)
    if ca[4] != cb[4]:
        if ca[4] > cb[4]:
            print("A")
        else:
            print("B")
    elif ca[3] != cb[3]:
        if ca[3] > cb[3]:
            print("A")
        else:
            print("B")
    elif ca[2] != cb[2]:
        if ca[2] > cb[2]:
            print("A")
        else:
            print("B")
    elif ca[1] != cb[1]:
        if ca[1] > cb[1]:
            print("A")
        else:
            print("B")
    else:
        print("D")


