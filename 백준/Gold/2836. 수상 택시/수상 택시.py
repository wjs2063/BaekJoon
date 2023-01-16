import sys
input = sys.stdin.readline

n,m = map(int,input().split())

line = []

for _ in range(n):
    start,end = map(int,input().split())
    # 어차피 0 -> M 까지는 가야함 가는김에 정방향애들 다태워서보내
    if start < end :continue
    line.append((start,end))
# 어차피 가야함
answer = m
# 역순정렬
line.sort(key = lambda x:(-x[0],-x[1]) )

sn,en = line[0]
# 역방향 계산
for i in range(1,len(line)):
    # 오른쪽에서 왼쪽으로 가는 것이니까
    # 다음 손님의 출발지점이 도착지점보다 오른쪽에있으면 ( 같아도됨)
    if line[i][0] >= en :
        if line[i][1] < en:
            en = line[i][1]
    # 만약 겹치지않으면
    else:
        # 이때까지 온 길이 더해주고
        answer += abs(sn - en) * 2
        # 출발지점 다시 세팅
        sn ,en = line[i]
answer += abs(sn - en) * 2
print(answer)


