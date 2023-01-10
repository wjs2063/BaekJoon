import sys
input = sys.stdin.readline

n = int(input().strip())

coin = []
for _ in range(n):
    x = list(input().strip())
    x = list(map(int,x))
    coin.append(x)
dp = [[[0]*(1 << 15) for _ in range(10)] for _ in range(n + 1)]
# coin[i][j] := 의미 -> j번째 예술가가 i번쨰 예술가에게 그림을 살때 가격

# 그림을 소유했던사람의 최댓값

# dp[현재아티스트][현재그림가격][state] := state 상태
# 똑같은 상태라도 5 3 1 순으로 온것과 1 3 5 온것은 price 가 다를수도있다 ( 대칭그래프가아님)


answer = 1
# 0번쨰사람과 state 1에서 시작한다
# dfs(i,state,price,cnt,prev) := 그림이 prev사람에게서왔으며 cnt명이 거쳐갔고 현재 i번째사람이 그림을 가지고있고, 상태가 state 이며 가격은 price
def dfs(i,state,price,cnt):
    global dp
    global coin
    global answer
    # 이미 방문했던 상태라면 -> dfs 구조로 이미 탐색했을테니까
    # cnt 명의 사람이 이전에 같은사람과 같은 상태로 왔었다면 패스
    if dp[i][price][state]:
        return
    answer = max(answer,cnt)
    dp[i][price][state] = 1
    # for 문 돌면서 현상태에서 어떤사람이 살수있는지 조사합니다. ( bitmask)

    # 효율이 제일 좋은 사람부터 확인해봅시다. 이전에 코인을 가격순으로 정렬해놓았으니
    for j in range(n):
        #자기자신한테 팔수없으므로 패스합니다
        if i == j :
            continue
        # j번째 사람이 이미 그림을 구매한 경우는 pass 해줍니다
        if state & ( 1 << j):
            continue
        # j번째사람은 그림을 구매한적이없고 , 팔수있는 경우라면
        if coin[i][j] >= price:
            # 다음그림은 j가 소유하고 상태 추가해주고, 가격은 coin[i][j], 거친사람은 cnt + 1이됨.
            dfs(j,state | (1 << j),coin[i][j],cnt + 1)
dfs(0,1,0,1)
print(answer)


"""
test case
2
12
12
정답 : 2 

3
000
000
000
정답 : 3


"""


