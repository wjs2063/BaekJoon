import sys
input = sys.stdin.readline

n = int(input().strip())

ball = [0,1,2,3]

for _ in range(n):
    a,b = map(int,input().split())
    # swap
    ball[a],ball[b] = ball[b],ball[a]

for i in range(1,4):
    if ball[i] == 1:
        print(i)