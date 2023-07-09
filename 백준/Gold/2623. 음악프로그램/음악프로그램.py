import sys
from collections import defaultdict,deque
input = sys.stdin.readline

n,m = map(int,input().split())
indegree = [0] * (n + 1)
tree = defaultdict(set)
vis = set()
for _ in range(m):
    arr = list(map(int,input().split()))[1:]
    for i in range(len(arr) - 1):
        tree[arr[i]].add(arr[i + 1])
    for i in range(len(arr) - 1):
        if (arr[i],arr[i + 1]) in vis:continue
        vis.add((arr[i],arr[i + 1]))
        indegree[arr[i + 1]] += 1


q = deque([])

order = []
for i in range(1,n + 1):
    if indegree[i] == 0 :
        q.append(i)

while q:
    root = q.popleft()
    order.append(root)
    for adj_node in tree[root]:
        indegree[adj_node] -= 1
        if indegree[adj_node] == 0:
            q.append(adj_node)
if len(order) == n :
    for item in order:
        print(item)
else:
    print(0)





