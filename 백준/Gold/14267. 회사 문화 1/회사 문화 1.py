import sys
sys.setrecursionlimit(10**6)
from _collections import defaultdict
input = sys.stdin.readline

n,m = map(int,input().split())

cc = list(map(int,input().split()))
tree = [[] for _ in range(n + 1)]
compliment = defaultdict(int)
# tree 추가
for i in range(len(cc)):
    senior = cc[i]
    if senior == - 1:
        continue
    tree[senior].append(i + 1)
ans = [0]*(n + 1)
def dfs(root,comp):
    global tree
    global answer
    if tree[root] == None:
        return
    ans[root] += comp
    for child in tree[root]:
        dfs(child,comp)
for _ in range(m):
    a,b = map(int,input().split())
    compliment[a] += b
for x in compliment:
    dfs(x,compliment[x])
print(*ans[1:])

