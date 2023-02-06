import sys
sys.setrecursionlimit(10**6)
from _collections import defaultdict
input = sys.stdin.readline
n,s,d = map(int,input().split())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
res = 0
def dfs(root,parent):
    global res
    depth = 0
    for next_node in tree[root]:
        if next_node == parent:continue
        depth = max(depth,dfs(next_node,root))
    # depth 가 d 이상인것들은 다 방문을 해야한다.
    if depth >= d:
        res += 1
    return depth + 1

dfs(s,-1)
# 3개방문이면 거리는 2이므로
# 만약 res 가 0이면 0을 출력
print(2*(res - 1) if res else 0)
