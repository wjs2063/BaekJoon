import sys
input = sys.stdin.readline

k = int(input().strip())

dir = dict()
dir[1] = (0,1)
dir[2] = (0,-1)
dir[3] = (1,0)
dir[4] = (-1,0)

pos = [[0,0]]
l_x,l_y = 0,0
r_x,r_y = 0,0
for _ in range(6):
    dirs,depth = map(int,input().split())
    x,y = pos[-1]
    # 방향만큼
    nx,ny = x + dir[dirs][0] * depth , y + dir[dirs][1] * depth
    #좌상단 우하단 기록
    l_x,l_y = min(l_x,nx),min(l_y,ny)
    r_x,r_y = max(r_x,nx),max(r_y,ny)
    pos.append([nx,ny])

mid_x,mid_y = 0,0
# 안쪽점 찾기

for x,y in pos:
    if l_x < x < r_x and l_y < y < r_y :
        mid_x,mid_y = x,y

# 바깥점 찾기

c = [(l_x,l_y),(l_x,r_y),(r_x,l_y),(r_x,r_y)]

for i,v in enumerate(c):
    flag = False
    for x,y in pos:
        if v == (x,y):
            flag = True
            break
    if not flag:
        out_x,out_y = v
#print(pos)
#print(mid_x,mid_y,out_x,out_y)

ans = (r_x - l_x ) * (r_y - l_y) - abs(mid_x - out_x) * abs(mid_y - out_y)

ans *= k

print(ans)
