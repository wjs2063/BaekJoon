import sys
input = sys.stdin.readline

n = int(input())

D = []
for _ in range(n):
    D.append(list(map(int,input().split())))
# n명의 사람과 n개의 일이 있다
INF = int(1e9)
dp = [[INF]*(1 << (n + 1)) for _ in range(n + 1)]
# D[i][j] i번째사람이 j번 일을 할때 필요한 비용
# dp[i][state] := i명인사람이 state 상태일때 최소비용
# dp[i][state] 일때
# state 에서 0인부분을 맡아가면서 dfs 탐색

# 0명,state 0 일때는 첫번째 사람이 모든일을 다 한번씩 해볼수있음 각경우마다 dfs
# 1번이 state 상태의 일을 맡았을때 최솟값 dp[i][state]
# 2번이


# dfs(i,state)  := i명의 사람이 state 상태의 일을 맡았을때의 값
def dfs(i,state):
    global dp
    # 사람이 n 이면 종료해주고
    if i == n:
        return 0
    # i,state 상태를 방문했으면 그대로반환
    if dp[i][state] != INF:
        return dp[i][state]
    rr = INF
    for k in range(1,n + 1):
        if state & ( 1 << k) == 0:
            # dfs 탐색 i번쨰 비트 켜주고 다음상태로 넘어가보자
            rr = min(rr,dfs(i + 1,state | ( 1 << k) ) + D[i - 1][k - 1] )
    dp[i][state] = rr
    return dp[i][state]
print(dfs(0,0))