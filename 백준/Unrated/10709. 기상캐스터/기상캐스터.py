import sys
input = sys.stdin.readline


n,m = map(int,input().split())

board = []

arr = [[-1]*m for _ in range(n)]
pos = [[] for _ in range(n)]
for i in range(n):
    board.append(input().strip())
    for j in range(m):
        if board[i][j] == "c":
            pos[i].append(j)
            arr[i][j] = 0

for i in range(n):
    while pos[i]:
        x,y = i,pos[i].pop()
        time = 0
        while y < m:
            # pass 하는 경우
            if arr[x][y] == -1:
                arr[x][y] = time
            y += 1
            time += 1
for i in range(n):
    print(*arr[i])

