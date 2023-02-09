import sys
import heapq
input = sys.stdin.readline

n,m,l = map(int,input().split())

arr = [0] + list(map(int,input().split())) + [l]
sn,en = 1,l
arr.sort()
ans = 0
while sn <= en:
    # 휴게소간 허용가능한 최대간격거리
    mid = (sn + en) // 2
    cnt = 0
    for i in range(len(arr) - 1):
        # 간격이 크면 휴게소설치
        if arr[i + 1] - arr[i] > mid:
            # ex 3과 10 사이 2간격 -> 5 ,7,9 3개
            # 3과 11 사이 2간격 -> 5,7,9 3개
            cnt += (arr[i + 1] - arr[i] - 1) // mid
    if cnt > m:
        # 휴게소가 많이 설치되어있으면 간격을 늘려서 줄이자
        sn = mid + 1
    else:
        en = mid - 1
        ans = mid

print(ans)
