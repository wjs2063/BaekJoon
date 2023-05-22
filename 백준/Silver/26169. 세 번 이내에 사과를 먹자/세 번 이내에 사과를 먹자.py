import sys
input = sys.stdin.readline

board = []

for _ in range(5):
    b = list(map(int,input().split()))
    board.append(b)

x,y = map(int,input().split())
flag = 0
def dfs(x,y,apple,dist):
    global flag
    if flag or dist > 3 :return
    apple += (board[x][y] == 1)

    if apple >= 2:
        flag = 1
        return
    temp = board[x][y]
    board[x][y] = -1
    for nx,ny in [(x + 1,y),(x - 1,y),(x,y + 1),(x,y - 1)]:
        if not (0 <= nx < 5 and 0 <= ny < 5):continue
        if board[nx][ny] == -1:continue
        dfs(nx,ny,apple,dist + 1)
    board[x][y] = temp
dfs(x,y,0,0)

if flag:
    print(1)
else:
    print(0)
