import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().strip())

info = defaultdict(list)

dp = [[0,1] for _ in range(n + 1)]

for _ in range(n - 1):
    u,v = map(int,input().split())
    info[u].append(v)
    info[v].append(u)


def dfs(root,parent):
    # 현재 노드가,얼리어답터인경우 dp[root][1]
    # dp[root][0]

    for child in info[root]:
        if child == parent:continue
        dfs(child,root)
        dp[root][1] += min(dp[child][0],dp[child][1])
        dp[root][0] += dp[child][1]

dfs(1,-1)

print(min(dp[1]))





