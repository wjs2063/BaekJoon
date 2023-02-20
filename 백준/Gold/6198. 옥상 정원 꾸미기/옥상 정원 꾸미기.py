import sys
input = sys.stdin.readline


n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(int(input().strip()))

stack = []
ans = 0
# stack 의 정의
# len(stack) := 현재빌딩의 옥상을 볼수있는 이전빌딩들의 개수
# 즉 나보다 큰애들만 내머리를 볼수있다.
# stack 에는 나보다 큰애들만 넣어야함.
for i,v in enumerate(arr):
    # stack 의 최상단에있는 건물이 현재 들어갈 원소보다 작다면
    while stack and stack[-1] <= v :
        stack.pop()
    ans += len(stack)
    stack.append(v)
print(ans)