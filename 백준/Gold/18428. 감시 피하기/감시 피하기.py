import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

board = []

for _ in range(n):
    board.append(list(input().split()))


cases = [(i,j) for i in range(n) for j in range(n)]
ccc = combinations(cases,3)

teachers = []

for r in range(n):
    for c in range(n):
        if board[r][c] == "T":
            teachers.append((r,c))

def check_empty_board(board,cc):
    for c in cc :
        x,y = c
        if board[x][y] != "X":
            return 0
    return 1
ans = 0

def solution(board,cc,teachers):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    # 모든 teachr 좌표에 대해서 조사한다.
    vis = set()
    for teacher in teachers:
        x,y = teacher
        for i in range(4):
            # 현재 방향에 대해서 쭉 전진한다
            for k in range(1,n + 1):
                nx = x + k * dx[i]
                ny = y + k * dy[i]
                if not (0 <= nx < n and 0 <= ny < n) :break
                if (nx,ny) in vis :continue
                # 장애물이면 패스
                if (nx,ny) in cc:break
                # 학생만나면
                if board[nx][ny] == "S":return 0
                vis.add((nx,ny))
    return 1



for cc in ccc:
    if not check_empty_board(board,cc):continue
    if solution(board,cc,teachers):
        ans = 1
        break


if ans :
    print("YES")
else:
    print("NO")

