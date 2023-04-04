import sys
input = sys.stdin.readline


n,m = map(int,input().split())

p = list(map(int,input().split()))

info = []

INF = int(1e10)
for _ in range(n - 1):
    info.append(list(map(int,input().split())))

dp = [0]*(n + 1)

for i in range(m - 1):
    src,dest = p[i],p[i + 1]
    if src > dest:
        src,dest = dest,src
    dp[src] += 1
    dp[dest] -= 1

for i in range(1,n + 1):
    dp[i] += dp[i - 1]
ans = 0
for i in range(1,n):
    # dp[i] : i번철도 이용횟수
    a,b,c = info[i - 1]
    ans += min(b*dp[i] + c,a*dp[i])
print(ans)
# IC 카드를 샀을때는 고정비용 + IC 비용
# IC 카드를 사지않았을때는 그냥 티켓비용
# 즉 고정비용 + IC 비용*(이용횟수) < 티켓비용 이면 IC 카드를 사고 , 아니면 사지말자




