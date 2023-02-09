import sys
sys.setrecursionlimit(10**7)
from collections import defaultdict
input = sys.stdin.readline

n = int(input().strip())
tree = defaultdict(list)
for _ in range(n - 1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
INF = int(1e10)
dp = [[0,1] for _ in range(n + 1)]
#초기값 세팅
dp[1][0] = 0
dp[1][1] = 1

#dp[i][0] -> i 번쨰 노드가 얼리어답터가 아닌경우 최솟값
#dp[i][1] -> i 번쨰 노드가 얼리어답터 인경우 최솟값

def dfs(root,parent):
    # root 가 얼리어답터인경우와 , 얼리어답터가 아닌경우 2가지로 나눠서 진행
    for child in tree[root]:
        if child == parent:continue
        # root가 얼리어답터 일경우 root가 얼리어답터가 되지않을수도,될수도
        dfs(child,root)
        dp[root][1] += min(dp[child][0],dp[child][1])
        # root가 얼리어답터가 아닌경우에는 child 는 무조건 얼리어답터여야한다
        dp[root][0] += dp[child][1]
dfs(1,-1)

print(min(dp[1]))
