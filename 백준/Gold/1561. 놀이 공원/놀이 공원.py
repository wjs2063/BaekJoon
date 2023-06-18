import sys
input = sys.stdin.readline

n,m = map(int,input().split())


play = list(map(int,input().split()))

sn,en = 1,int(2e9) * 30
total_time = 0


while sn <= en :
    mid = (sn + en) // 2
    # mid 시간으로 모든사람을 다 태울수있는가?
    cnt = 0

    for i,v in enumerate(play):
        # i번째 기구를 타는데 걸리는 시간
        cnt += mid // v + 1
    # cnt 태울수있는 사람수
    if cnt >= n :
        total_time = mid
        en = mid - 1
    else:
        sn = mid + 1
# 총 total_time 시간이 걸린다 .

# 운행시간은 1이상 30 이하의 자연수이므로
# total_time - 1 만큼일때 탈수있는 사람들을 구한다

cnt = 0

if n <= m :
    print(n)
else:
    for i,v in enumerate(play):
        # 0분부터 시작
        # 15 15 20 30 40
        # 첫 14분까지 5명바로 탑승가능
        cnt += (total_time - 1) // v + 1
    for i,v in enumerate(play):
        if total_time % v == 0 :
            cnt += 1
        if cnt == n :
            print(i + 1)
            break

