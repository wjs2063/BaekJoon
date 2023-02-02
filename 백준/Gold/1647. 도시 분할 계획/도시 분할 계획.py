import sys
input = sys.stdin.readline
n,m = map(int,input().split())

graph = []

for _ in range(m):
    a,b,c = map(int,input().split())
    graph.append((c,a,b))

parent = [i for i in range(n + 1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    x = find(a)
    y = find(b)
    parent[x] = y
# 최소비용순으로 정렬
graph.sort()
res = 0
m = 0
for i in range(len(graph)):
    cost,a,b, = graph[i]
    if find(a) != find(b):
        union(a,b)
        res += cost
        m = max(m,cost)

# 모든곳을 MST 트리로 만들었다 그러면 제일 낮은 가격하나 제외
print(res - m)