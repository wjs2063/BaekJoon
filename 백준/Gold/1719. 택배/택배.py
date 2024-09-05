import sys
from _collections import defaultdict

si = sys.stdin.readline

n, m = map(int, si().strip().split())
INF = int(1e10)

# 거리 기록
dp = [[INF] * (n + 1) for _ in range(n + 1)]
# 노드 기록 node[a][b] := a 에서 b 로가야할때 첫번쨰로 진입해야할 노드
node = [['-'] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, si().strip().split())
    dp[a][b] = c
    dp[b][a] = c
    node[a][b] = str(b)
    node[b][a] = str(a)

for k in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if start == end: continue

            if dp[start][k] + dp[k][end] < dp[start][end]:
                dp[start][end] = dp[start][k] + dp[k][end]
                # start -> end 로 가기위해서는 start 에서 k 로 가야할 처음 진입점을 들러야한다.
                node[start][end] = node[start][k]

for i in range(1, n + 1):
    print(*node[i][1:])
