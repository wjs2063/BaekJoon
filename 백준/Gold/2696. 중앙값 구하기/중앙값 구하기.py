import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m = int(input().strip())
    arr = []
    for _ in range(m // 10 + 1):
        arr.extend(list(map(int,input().split())))
    # 힙
    # left 에는 최대힙 ,right 에는 최소힙
    # 항상 left <= right 으로 유지하되 최대 1개차이만 나도록 구성한다
    left, right = [] , []
    res = []
    for i in range(len(arr)):
        if len(left) == len(right):
            heapq.heappush(left,-arr[i])
        else:
            heapq.heappush(right,arr[i])

        # 항상 left <= right 이 유지되게 증 이으면 정렬이 되게유지
        if left and right and -left[0] > right[0]:
            x = -heapq.heappop(left)
            y = heapq.heappop(right)
            # 최대힙이니까 부호신경써주고
            heapq.heappush(left,-y)
            heapq.heappush(right,x)
        # 만약 홀수개라면
        if i % 2 == 0:
            res.append(-left[0])
    print(len(res))
    print(*res)
