import sys
input = sys.stdin.readline

n = int(input())


for _ in range(n):
    xx,yy = input().split()
    dist = []

    for i,v in enumerate(xx):
        if ord(yy[i]) >= ord(v):
            dist.append(ord(yy[i]) - ord(v))
        else:
            dist.append(26 + ord(yy[i]) - ord(v))

    print("Distances:",*dist)