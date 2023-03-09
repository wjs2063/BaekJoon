import sys
input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())

grid = []

for _ in range(n):
    grid.append(list(map(int,input().split())))
"""
기본 베이스 1,2,3,4,5,6
1번 : 4 2 1 6 5 3
2번 3 2 6 1 5 4 
3번 5 1 3 4 6 2
4번 2 6 3 4 1 5
"""
#위는 인덱스변화임
# 1 ~ 6까지



dice = [0]*6
# 항상 0번쨰 인덱스가 위 5번째 인덱스가 아래이다

commands = list(map(int,input().split()))

h = {
    1:(0,1),
    2:(0,-1),
    3:(-1,0),
    4:(1,0)
}

for command in commands:
    dx,dy = h[command]
    nx,ny = x + dx,y + dy
    if nx < 0 or nx >= n or ny < 0 or ny >= m:continue
    if command == 1:
        dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    elif command == 2:
        dice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    elif command == 3:
        dice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    else:
        dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    if grid[nx][ny] == 0:
        grid[nx][ny] = dice[5]
    else:
        dice[5] = grid[nx][ny]
        grid[nx][ny] = 0
    x,y = nx,ny
    print(dice[0])

