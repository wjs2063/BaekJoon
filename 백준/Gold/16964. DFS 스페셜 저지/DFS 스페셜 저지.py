import sys
sys.setrecursionlimit(10**5)
from _collections import defaultdict,deque
input = sys.stdin.readline

n = int(input().strip())

graph = defaultdict(list)

for _ in range(n - 1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

path = list(map(int,input().split()))

time = [0]*(n + 1)
# 방문시간을 적어둔다.
for i,v in enumerate(path):
    time[v] = i + 1
# time[x] := x라는 노드를 방문한 시점을 의미한다
# dfs 를할떄 어떤것을 방문할지 모르잖아? 그거를 방문시점으로 정렬해서 정해주는거지
# 모든 노드에대해서 방문시점순으로 정렬해준다
for v in graph:
    graph[v].sort(key = lambda x : time[x])

temp = []

def dfs(node,graph,visited):
    if visited[node] :return
    temp.append(node)
    visited[node] = 1
    for next_node in graph[node]:
        dfs(next_node,graph,visited)

dfs(1,graph,[0]*(n + 1))
if temp == path:
    print(1)
else:print(0)


