import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[-1,-1]]

for _ in range(n ):
    l,r = map(int,input().split())
    graph.append([l,r])
k = int(input().strip())
# graph[i] := 의미 graph[i]의 왼쪽은 graph[i][0] , graph[i][1]
# root 는 항상 1번

# dp[i] : i번째 노드의 서브트리 구슬의 총합

# k번쨰 구슬이 어떤노드에서 멈춰?? 이분탐색같음, 범위가 너무커
# 결국 리프노드에 떨어지게되니까 리프노드를 결정지어야하는데 

# k번째에 어떤노드에 떨어지게 된다면 다시말해서 k - 1번쨰 작업으로 그 노드까지갈수있는 경로를 만들어야함
# 이것은 트리의 상황에따라 결정되어진다

# 예를들면 100 을 -> 50,50 으로 나누거나 101을 51 50 으로 나눌수있다. ( 항상 L >= R 이성립함)
# 1에서 시작해서 왼쪽에 50 오른쪽 50 주고 또 그 50을 나눠서 재귀적으로 분배시켜준다
# log k 만큼 걸리겠지 그리고 나서 마지막에 떨어뜨려서 최종적으로 확인하면된다

#
# k -1 을 분배시키자

dp = [0 for _ in range(n + 1)]
# num 에는 k - 1이 들어가야함
def dfs(graph, num,root ):
    global dp
    # 저장할 게없으면 종료
    if num == 0:
        return
    # 현재 노드에 저장
    dp[root] = num
    left_ch,right_ch = graph[root]
    #자식이 존재하지않으면 현재노드에 저장하고 종료
    if left_ch == -1 and right_ch == -1:
        return
    #num 을 연속된 두 자연수의 합으로 분할 ( 단 L >= R 이 지켜져야함 )
    q,r = divmod(num,2)
    l,r = q + r,q
    # 왼쪽자식이 비어있으면 오른쪽에몰빵
    if left_ch == -1:
        dfs(graph,num,right_ch)
    # 오른쪽이 비어있으면 왼쪽에 몰빵
    elif right_ch == -1:
        dfs(graph,num,left_ch)
    else:
        #재귀적으로 수행
        dfs(graph,l,left_ch)
        dfs(graph,r,right_ch)
# 수행한번 해주고
dfs(graph,k - 1,1)
# 어디에 떨어질지 이제 체크만해주면된다

# check_dfs 의미 -> root 에서 해당 규칙을따라 어떤 리프노드로 떨어지는지 반환
def check_dfs(graph,root):
    global dp
    l,r = graph[root]
    # 1번규칙
    if l == -1 and r == -1 :
        print(root)
        return
    # left,right 은 root 의 왼쪽,오른쪽서브트리에 담긴 구슬의 총합
    # 2번규칙
    if l == -1 :
        check_dfs(graph,r)
    elif r == -1 :
        check_dfs(graph,l)
    else:
        # 자식노드가 두개라면
        left,right = dp[l],dp[r]
        if left <= right:
            check_dfs(graph,l)
        else:
            check_dfs(graph,r)

check_dfs(graph,1)
