import sys
input = sys.stdin.readline

n = int(input().strip())

info = [[] for _ in range(n**2 + 1)]

vis = [[0]*(n + 1) for _ in range(n + 1)]
# info[x] := x 번째학생이 좋아하는 학생들의 번호
seq = []
for _ in range(n**2):
    x = list(map(int,input().split()))
    info[x[0]].extend(x[1:])
    seq.append(x[0])


cnt = n**2
def in_range(x,y):
    if 1<= x < n + 1 and 1 <= y < n + 1:return True
    return False

def favorite_friend(my_num,nx,ny):
    # 현재 나의 좌표 x,y
    # 친구번호
    friend_num = vis[nx][ny]
    if friend_num in info[my_num]:
        return 1
    return 0


# 내가앉을 자리 찾기
def empty_seat(my_num):
    seat = []
    max_adj = 0
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            # 이미 좌석에앉아있으면 패스해주고
            if vis[i][j] : continue
            # 인접친구 계산
            adj_friends = 0
            empty = 0
            for nx,ny in [(i + 1,j),(i - 1,j),(i,j + 1),(i,j - 1)]:
                if in_range(nx,ny):
                    if vis[nx][ny] == 0:
                        empty += 1
                    adj_friends += favorite_friend(my_num,nx,ny)
            # 인접친구수,x좌표,y좌표
            max_adj = max(max_adj,adj_friends)
            seat.append([empty,adj_friends,i,j])
    sub = []
    for i,v in enumerate(seat):
        if v[1] == max_adj:
            sub.append(v)
    return sub

def adj_seat(seat):
    seat.sort(key = lambda x:(-x[0],x[2],x[3]))
    return seat
for my_num in seq:
    seat = empty_seat(my_num)
    # 1개이상이면

    if len(seat) > 1:
        seat = adj_seat(seat)
    x,y = seat[0][2],seat[0][3]
    vis[x][y] = my_num

ans = 0
for x in range(1,n + 1):
    for y in range(1,n + 1):
        # 만족도를 구해볼 학생넘버
        my_num = vis[x][y]
        ff = 0
        for nx,ny in [(x + 1,y),(x - 1,y),(x, y + 1),(x, y - 1)]:
            if in_range(nx,ny):
                ff += favorite_friend(my_num,nx,ny)
        if ff == 1:
            ans += 1
        elif ff == 2:
            ans += 10
        elif ff == 3:
            ans += 100
        elif ff == 4:
            ans += 1000
print(ans)
