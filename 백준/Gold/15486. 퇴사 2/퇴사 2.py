import sys
input = sys.stdin.readline

n = int(input())

t = [0]
p = [0]

for _ in range(n):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)

dp = [0]*(n + 1)
# 상담을 쓰는경우 안쓰는경우 두가지?
# dp[i] i번째 날까지 얻을수있는 최댓값
for i in range(1, n + 1):
    # 만약 퇴사날짜까지 상담가능하면 해당 상담일정을 쓸수도있고 쓰지않을수도있다.
    # 한번 쓰면 i <= x < i + t[i] 사이 날짜에서는 다른일정을 잡지못한다
    # 일단 이전값들중 최댓값으로 갱신하고
    dp[i] = max(dp[i],dp[i - 1])
    # 퇴사전까지 끝낼수있는 일이라면
    if i + t[i] - 1 <= n :
        # 안썻을때와 i - 1일째까지 최댓값에서 i번쨰일을 할떄 둘중 최댓값
        dp[i + t[i] - 1] = max(dp[i + t[i] - 1 ],dp[i - 1] + p[i])
print(dp[n])
# 예제를보면 1일에 시작하는게 1 2 3 -> 3일에 끝난다 1(시작) + 3(소요시간) - 1 ->  3일 
# 