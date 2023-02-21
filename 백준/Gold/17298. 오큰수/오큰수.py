import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

stack = []

dp = [-1]*(n)
# stack 정의
#
for i,v in enumerate(arr):
    # stack 의 최상단에 있는값이 현재값보다 작다면
    # stack 최상단값의 기준에서는 오큰수가된다.
    while stack and stack[-1][0] < v:
        val,idx = stack.pop()
        dp[idx] = v
    # 현재값과 idx 를 넣고
    stack.append([v,i])
print(*dp)