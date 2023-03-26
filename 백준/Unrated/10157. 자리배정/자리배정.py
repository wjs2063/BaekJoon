import sys
input = sys.stdin.readline

m,n = map(int,input().split())
num = int(input().strip())

a  = [[0]*m for _ in range(n)]

def in_range(x,y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False
if num > m * n :
    print(0)
else:
    s = 1
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    i = 0
    x,y = 0,0
    ans = [0,0]
    while num:
        if not in_range(x,y) or a[x][y]:
            x,y = x - dirs[i][0],y - dirs[i][1]
            i = (i + 1) % 4
            x,y = x + dirs[i][0],y + dirs[i][1]
            continue
        a[x][y] = s
        s += 1
        num -= 1
        ans = [y + 1,x + 1]
        x,y = x + dirs[i][0],y + dirs[i][1]
    print(*ans)
