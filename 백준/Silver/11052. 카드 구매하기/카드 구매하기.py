import sys
input = sys.stdin.readline

n = int(input().strip())

card = [0] + list(map(int,input().split()))
dp = [0] + [card[i] for i in range(1,n + 1)]
# 1,2,3,4,  ... N 개의 카드팩이있다.
# x + 2y + 3z + 4w ... na = N 이 되어야한다

# n 개를 살때
# dp[i] := i개의 카드를 샀을떄의 최댓값
# i번쨰 카드일떄 1 <= j < i 카드를 돌면서 어떤거를 추가할떄 이득인지 체크
for i in range(1,n + 1):
    for j in range(1,i):
        dp[i] = max(dp[i],dp[i - j] + card[j])
print(dp[n])