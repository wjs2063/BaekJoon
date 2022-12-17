import sys
from collections import deque
from itertools import combinations
import copy
input = sys.stdin.readline

n,m,d = map(int,input().split())
origin_castle = deque([])
answer = 0
for _ in range(n):
    origin_castle.append(deque(map(int,input().split())))

def detect(castle,bow):
    x,y = bow
    near = []
    for i in range(n - 1,-1,-1):
        for j in range(m):
            distance  = abs(x - i) + abs(y - j)
            if castle[i][j] == 1 and distance <= d:
                near.append((distance,i,j))
    if near:
        near.sort(key = lambda x: (x[0],x[2]))
        return near[0][1:]
    return -1,-1
def attack(castle,bower):
    global sub
    cc = set()
    for bow in bower:
        nx,ny = detect(castle,bow)
        if nx == -1 and ny == -1:
            continue
        cc.add((nx,ny))
    for c in cc :
        x,y = c
        castle[x][y] = 0
        sub += 1
def down(castle):
    castle.pop()
    castle.appendleft(deque([0]*m))
cc = combinations([(n ,i) for i in range(m)],3)

for bower in cc:
    sub = 0
    castle = copy.deepcopy(origin_castle)
    for _ in range(n):
        attack(castle,bower)
        down(castle)
    answer = max(answer,sub)
print(answer)