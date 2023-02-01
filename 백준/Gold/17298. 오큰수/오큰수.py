import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))
# stack 에는 index 를 넣는다
stack = []

dp = [-1]*n
# 원리를 살펴보면

# stack 에 뭐가 들어있으며 stack 의 최상단에는 이전중 최신 index 가들어있다
# 이 인덱스에 해당하는 값이 만약 현재살펴볼 arr[i] 보다 작으면
# 그말 즉 -> 오른쪽중 가장 왼쪽에있는 값이된다 -> arr[i]가
# 이것을 반복적으로 돌리면서 index에 추가한다

# 일단 stack 에 index 를 추가한다
for i in range(n):
    # stack 최상단에 위치한 값이 현재 값 보다 작으면
    while stack and arr[stack[-1]] < arr[i]:
        dp[stack.pop()] = arr[i]
    stack.append(i)
print(*dp)


