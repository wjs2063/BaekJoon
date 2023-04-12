import sys
from itertools import product
input = sys.stdin.readline

n,k,c = map(int,input().split())

A = list(map(int,input().split()))

pp = product([i for i in range(n)],repeat = c)
ans = float("inf")
seen = set()
for p in pp :
    # A 복사하고
    a = A[:]
    # p 에는 격려해줄 요리사의 인덱스가 담겨있다
    for _,v in enumerate(p):
        a[v] = max(1,a[v] - 1)
    # 이전에 진행한경우면 패스
    if tuple(a) in seen:continue
    seen.add(tuple(a))
    sn,en = 0,k * max(a)
    while sn <= en :
        # mid -> 주어진 시간
        mid = (sn + en) // 2
        food_cnt = 0
        # 주어진 시간내에 몇개의 음식을 만들수있을까?
        for _,v in enumerate(a):
            food_cnt += mid // v
        # 주어진 시간내에 k 개 이상을 만들수있어?
        if food_cnt >= k :
            if mid < ans :
                ans = mid
            # 가능하면 범위를 시간을 좀 더 줄여서 체크하자
            en = mid - 1
        else:
            sn = mid + 1
print(ans)

