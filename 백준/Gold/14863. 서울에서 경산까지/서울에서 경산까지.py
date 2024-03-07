import sys

si = sys.stdin.readline

n, k = map(int, si().split())

walk = [[0, 0]]
bike = [[0, 0]]
for _ in range(n):
    a, b, c, d = map(int, si().split())
    walk.append([a, b])
    bike.append([c, d])

# dp[a][b] := 현재 a 번도시이며 남은시간은 b 라고 가정할때 모을수있는 최대 금액
# dp[0][k] := 현재 0 번도시이고 남은시간은 k 이다
INF = int(1e10)
dp = [[-INF] * (k + 1) for _ in range(n + 1)]


def sol(cur, rest) -> int:
    # 현재가 0번도시면 넌 모을수있는 금액이없어요
    if cur == 0: return 0
    # 이미 계산된건 그대로 리턴
    if dp[cur][rest] != -INF:
        return dp[cur][rest]
    # 도보
    if rest - walk[cur][0] >= 0:
        dp[cur][rest] = max(dp[cur][rest], sol(cur - 1, rest - walk[cur][0]) + walk[cur][1])
    # 자전거
    if rest - bike[cur][0] >= 0 :
        dp[cur][rest] = max(dp[cur][rest],sol(cur - 1,rest - bike[cur][0]) + bike[cur][1])
    return dp[cur][rest]

print(sol(n,k))