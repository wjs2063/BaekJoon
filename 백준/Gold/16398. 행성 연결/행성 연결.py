import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n = int(input())
INF = int(1e9)
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

parent = [i for i in range(n)]
def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    x = find(a)
    y = find(b)
    parent[x] = y
cost = []
for i in range(n):
    for j in range(n):
        cost.append((matrix[i][j],i,j))
cost.sort()
res = 0
for c,x,y in cost:
    if find(x) == find(y):continue
    union(x,y)
    res = max(res,res + c)
print(res)