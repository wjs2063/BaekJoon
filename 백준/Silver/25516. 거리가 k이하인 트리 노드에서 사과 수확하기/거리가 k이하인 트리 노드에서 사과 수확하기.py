import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
input = sys.stdin.readline

n,k = map(int,input().split())


grp = defaultdict(list)

for _ in range(n - 1):
    x,y = map(int,input().split())
    grp[x].append(y)
    grp[y].append(x)

info = list(map(int,input().split()))
ans = 0
def dfs(root,dist,parent):
    global ans
    if dist > k : return
    ans += (info[root] == 1)
    for next_node in grp[root]:
        if next_node == parent:continue
        dfs(next_node,dist + 1,root)
dfs(0,0,-1)
print(ans)
