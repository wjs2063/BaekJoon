import sys
input = sys.stdin.readline

n,c = map(int,input().split())

house = []

for _ in range(n):
    house.append(int(input().strip()))
house.sort()

sn,en = 1,house[-1] - house[0]
ans = 0
while sn <= en:
    # 공유기 사이의 최대 거리 mid
    mid = (sn + en) // 2
    # cnt 공유기 개수
    cnt = 1
    last = house[0]
    #print("start")
    for i in range(1,n):
        # last := 최근설치한 공유기 위치
        # 거리가 mid 보다 커지는순간 그자리에 공유기를 설치해야한다.
        if house[i] - last >= mid:
            #print(house[i])
            last = house[i]
            cnt += 1
    #print(sn,en,cnt)
    # 공유기를 적게 설치했다면
    if cnt < c :
        en = mid - 1
    else:
        ans = mid
        sn = mid + 1
print(ans)