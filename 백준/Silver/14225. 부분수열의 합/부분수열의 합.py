import sys
n = int(input())

arr = list(map(int,input().split()))
arr.sort()
# 첫번째 원소가 1이 냐 아니냐 먼저 체크
# 즉 dp[i] 와 arr[i] 사이에 수가 1개이상 존재하면안됨
# 이것을 arr[i] - dp[i - 1] <= 1 로 체크
def solve(n,arr):
    answer = 0
    for i in range(n):
        if arr[i] - answer > 1:
            return answer + 1
        answer += arr[i]
    return answer + 1
print(solve(n,arr))