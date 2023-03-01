import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input().strip()))

# 왼쪽에는 최대힙 오른쪽에는 최소힙
# 항상 길이는 l >= r 을 유지한다 -> 길이차이는 최대 1이다
left, right = [], []

res = []

for i in range(n):
    # 길이가 같으면 left 에
    if len(left) == len(right):
        heapq.heappush(left,-arr[i])
    else:
    # 다르면 오른쪽에
        heapq.heappush(right,arr[i])
    # left 원소 <= right 원소를 만족해야하므로
    if left and right and -left[0] > right[0]:
        x = -heapq.heappop(left)
        y = heapq.heappop(right)
        heapq.heappush(left,-y)
        heapq.heappush(right,x)
    # 항상 left[0] -> 중앙값으로 유지
    res.append(-left[0])
for i in range(len(res)):
    print(res[i])