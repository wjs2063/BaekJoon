import sys
sys.setrecursionlimit(10**5)
from collections import defaultdict
input = sys.stdin.readline
n,m = map(int,input().split())

grp = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    grp[b].append(a)
x = int(input())
ans = 0
seen = set()


def dfs(node):
    global ans
    ans += 1
    seen.add(node)

    for next_node in grp[node]:
        if next_node not in seen :
            dfs(next_node)

dfs(x)

print(ans - 1)