import sys
import heapq
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    arr = []
    left, right = [], []
    for _ in range(n // 10 + 1):
        arr.extend(list(map(int,input().split())))
    # 항상 길이를 left <= right 을 유지하면서
    # 모든 수들도 left <= right 을 유지하게 해보자
    # 길이차이는 항상 1이나게 할것이다
    # 중앙값은 항상 -left[0] 이 되도록 유지한다.
    answer = []
    for i in range(len(arr)):
        if len(left) <= len(right):
            heapq.heappush(left, -arr[i])
        else:
            heapq.heappush(right,arr[i])
        if left and right and  -left[0] > right[0]:
            x,y = heapq.heappop(left),heapq.heappop(right)
            x = -x
            heapq.heappush(right,x)
            heapq.heappush(left,-y)
        if left and i % 2 == 0:
            answer.append(-left[0])
    print(len(answer))
    for i in range(len(answer) // 10 + 1):
        print(*answer[10*i:10*i + 10])

