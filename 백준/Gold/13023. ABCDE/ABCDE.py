import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
input = sys.stdin.readline

n,m = map(int,input().split())

graph = defaultdict(list)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
flag = False
def dfs(graph,temp,i):
    global flag
    if len(temp) == 5 or flag:
        flag = True
        return
    for node in graph[i]:
        if node not in temp:
            dfs(graph,temp | {node},node)
for i in range(n):
    if not flag:
        dfs(graph,{i},i)

if flag:
    print(1)
else:
    print(0)
