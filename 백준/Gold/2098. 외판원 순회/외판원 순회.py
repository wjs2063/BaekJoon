import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

n = int(input().strip())

w = []
INF = float("inf")
for _ in range(n):
    w.append(list(map(int,input().split())))
dp = [[-1]*(1 << n) for _ in range(n)]
# 이전도시는 prev
# dp[start][state] i번째 도시를 방문,상태는 state 일때 최솟값

# dfs 의미 : 현재 node , 그리고 상태 state , node 까지 오는데 걸리는 비용
def dfs(node,state):
    if state == (1 << n) - 1 :
        if w[node][0] == 0:
            return INF
        else:
            return w[node][0]
    # 방문하지않은 지점이면
    if dp[node][state] != -1:
        return dp[node][state]
    mm = float("inf")
    for i in range(n):
        # 방문했던점이면 패tm
        if state & ( 1 << i):continue
        # 길이없는경우 패스
        if w[node][i] == 0:continue
        # node -> i 로 가는경우는
        dd = dfs(i,state | (1 << i)) + w[node][i]
        if dd < mm:
            mm = dd
    dp[node][state] = mm
    return dp[node][state]
print(dfs(0,1))