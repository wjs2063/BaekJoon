import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input().strip())

# x노드의 깊이
def dfs(x,depth):
    c[x] = 1
    d[x] = depth
    for child in graph[x]:
        if c[child] :continue
        dfs(child,depth + 1)

def lca(a,b):

    while d[a] != d[b]:
        # a 의 깊이가 더깊으면
        if d[a] > d[b] :
            a = parent[a]
        else:
            b = parent[b]
    # 현재 깊이 가같으면

    while a != b:
        a = parent[a]
        b = parent[b]
    return a

for _ in range(t):
    n = int(input().strip())
    graph = defaultdict(list)
    indegree = [0]*(n + 1)
    # 깊이
    d = [0]*(n + 1)
    # 체크
    c = [0]*(n + 1)
    parent = [0]*(n + 1)
    for _ in range(n - 1):
        p,ch = map(int,input().split())
        graph[p].append(ch)
        parent[ch] = p
        indegree[ch] += 1
    for i in range(1,n + 1):
        if indegree[i] == 0:
            root = i
            break
    dfs(root,0)
    a,b = map(int,input().split())
    print(lca(a,b))



