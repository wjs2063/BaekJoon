import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))


dp = [[float("-inf")]*2 for _ in range(n + 1)]

# dp[i][0] -> i 번쨰 수를 제거했을때[0] -> 안했을때 1
dp[0][1] = arr[0]
ans = max(dp[0])
for i in range(1,n):
    # 이전 누적합을 보자 -> i - 1번째 까지 누적합중 제거해서
    v = arr[i]
    # 특정원소를 제거하는경우 -> i - 1번째까지중 아무것도 제거하지않고 온경우 vs i - 1번째까지중 1개를 제거하고온경우
    dp[i][0] = max(dp[i - 1][1],dp[i - 1][0] + v)
    # 현재숫자를 넣ㄴㄴ경우는 이전경우와 상관없이 다 가능
    dp[i][1] = max(dp[i - 1][1] + v,v)
    ans = max(ans,max(dp[i]))
print(ans)


