import sys
from collections import defaultdict,deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,w = map(int,input().split())
tree = defaultdict(list)
for _ in range(n - 1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
# leve[x] -> 현재 x 레벨의 카운트 개수
level = defaultdict(int)
# 각 노드의 레벨
leaf = 0
def bfs(n):
    global leaf
    q = deque([1])
    visited = [0]*(n + 1)
    visited[1] = 1
    while q:
        x = q.popleft()
        # leaf 노드 카운트
        for next_node in tree[x]:
            if visited[next_node]:continue
            if len(tree[next_node]) == 1 and visited[x] == 1:
                leaf += 1
            visited[next_node] = 1
            q.append(next_node)
# bfs 돌리고
bfs(n)
print(w / leaf)