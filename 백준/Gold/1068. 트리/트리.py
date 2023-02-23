import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

parent = list(map(int,input().split()))

d_node = int(input().strip())
#parent[x] := x 번쨰노드의 부모노드
tree = defaultdict(list)
for i in range(len(parent)):
    if i == d_node:continue
    tree[parent[i]].append(i)
answer = 0
def dfs(root):
    # root 의 자식노드가없거나 -1 이아니라면
    if not tree[root] and root != -1:
        global answer
        answer += 1
        return
    for child in tree[root]:
        dfs(child)
dfs(-1)
print(answer)
