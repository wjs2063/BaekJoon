import sys
from collections import deque
input = sys.stdin.readline


board = []

for _ in range(19):
    board.append(list(map(int,input().split())))

vis = [[0]*19 for _ in range(19)]


ans = 0
a,b = -1,-1

def in_range(x,y):
    if 0 <= x < 19 and 0 <= y < 19:
        return 1
    return 0

dirs = [(0,1),(1,1),(1,0),(1,-1)]

def solve():
    for x in range(19):
        for y in range(19):
            if board[x][y] == 0 : continue
            color = board[x][y]
            for k in range(4):
                nx,ny = x + dirs[k][0],y + dirs[k][1]
                if not in_range(nx,ny):continue
                path = [(x,y)]
                #역방향
                ix,iy = x - dirs[k][0],y - dirs[k][1]
                while in_range(ix,iy) and board[ix][iy] == color:
                    path.append((ix,iy))
                    ix,iy = ix - dirs[k][0],iy - dirs[k][1]
                #정방향
                while in_range(nx,ny) and board[nx][ny] == color:
                    path.append((nx,ny))
                    nx,ny = nx + dirs[k][0],ny + dirs[k][1]
                if len(path) == 5:
                    path.sort(key = lambda t:(t[1],t[0]))
                    return color,path[0][0],path[0][1]
    return 0,0,0

ans,a,b = solve()

if ans:
    print(ans)
    print(a + 1,b + 1)
else:
    print(ans)



