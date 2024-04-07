import sys

si = sys.stdin.readline

n, m = map(int, si().split())

arr = list(map(int, si().split()))

"""
n <= 5,000
n개의 배열을 m개의 구간으로 나누는 방법 

mHn = (m + n - 1)C n -> 시초 

구간의 개수가 m개니까 

각 점수의 최댓값을 x 로두고 
이 x를 변경시켜가면서 구간이 m개가 넘으면 x를 줄여
m개보다 작으면 x 를 늘려 

"""

sn, en = 0, max(arr) - min(arr)
ans = 0
while sn <= en:
    mid = (sn + en) // 2

    # mid 만큼의 점수로 만들수있는 구간개수
    # 초기 min,max 값 정의
    l, r = int(1e10), 0
    # 구간의 개수 line_cnt = 1
    line_cnt = 1
    for i, v in enumerate(arr):
        if max(r, v) - min(l, v) > mid:
            #if i == len(arr) - 1:continue
            line_cnt += 1
            l, r = v, v
        else:
            l, r = min(l, v), max(r, v)

    if line_cnt > m:
        sn = mid + 1
    else:
        en = mid - 1
        ans = mid
print(ans)