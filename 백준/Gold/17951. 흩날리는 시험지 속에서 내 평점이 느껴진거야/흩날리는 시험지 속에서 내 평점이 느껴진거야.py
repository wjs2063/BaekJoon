import sys
input = sys.stdin.readline

n,k = map(int,input().split())

arr = list(map(int,input().split()))

# 모든 그룹이 가질수있는 최대 점수를 mid 로 놓고 mid 가 초과되기전까지 계속 그룹추가
# O(nlogn)
# 각 그룹의 문제합의 최솟값 -> 즉 최솟값을 최대화 시켜야함 .
sn,en = 0,20*n
ans = 0
while sn <= en:
    mid = (sn + en) // 2
    group = 0
    temp = 0
    for i in range(n):
        # 추가가능하면 추가
        temp += arr[i]
        if temp >= mid:
            temp = 0
            group += 1

    #마지막에도 갱신 -> 모든그룹이 mid 점수를 넘을수없고, mid 를 넘지않는 그룹의 점수집합에서 가장작은게 정답
    # 모든그룹의 문제합의 최솟값을 얻을수있으므로
    # 만약 그룹이 k 개가 초과됐으면  그룹을 줄여야하므로 점수를 높이는 방향으로 진행
    #print(sn,mid,en,group,sub)
    if group >= k :
        ans = mid
        sn = mid + 1
    # 그룹의 최솟값들이 mid 보다 크다면 또 줄여야함
    else:
        en = mid - 1
print(ans)

