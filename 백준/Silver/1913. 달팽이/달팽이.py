import sys
input = sys.stdin.readline
n = int(input())
val = int(input())

arr = [[-1] * n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
x,y = n // 2 , n // 2
num = 1
dirs = 0
cnt = 1
count = 0
# 위,오른쪽,아래,왼쪽 순으로 간다
k = 0
def in_range(x,y):
    if 0 <= x < n and 0 <=  y < n :return 1
    return 0

while num <= n ** 2 :
    arr[x][y] = num
    num += 1
    k += 1
    x,y = x + dx[dirs],y + dy[dirs]

    if k == cnt :
        dirs = (dirs + 1) % 4
        k = 0
        count += 1
        if count % 2 == 0 :
            cnt += 1
sx,sy = -1,-1
for i in range(n):
    print(*arr[i])
    for j in range(n):
        if arr[i][j] == val:
            sx,sy = i,j
print(sx + 1,sy + 1)
