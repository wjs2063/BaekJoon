import sys
input = sys.stdin.readline

n,k = map(int,input().split())

arr = list(map(int,input().split()))

c = []
# 차이 계산 ( 차이 == 비용)
for i in range(len(arr) - 1):
    c.append(arr[i + 1] - arr[i])
#
c.sort()
# 1 1 2 10 11 191 -> 3 개조
# 차이는 0 1 8 1 180
# 0 1 1 8 180
# 0 1 1 을 한개조로 묶고 8 180 짜리를 각각 1인1조로할당한다
# 즉 1
print(sum(c[:n - k]))
