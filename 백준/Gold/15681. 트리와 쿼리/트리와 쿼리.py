import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,r,q = map(int,input().split())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
dp = [0] * ( n + 1)

def dfs(tree,root):
    global dp
    dp[root] = 1
    for child in tree[root]:
        if dp[child] == 0:
            dfs(tree,child)
            dp[root] += dp[child]
dfs(tree,r)
qr = [int(input()) for _ in range(q)]

for q in qr:
    print(dp[q])


