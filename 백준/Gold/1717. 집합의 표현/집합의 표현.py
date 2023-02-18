import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())


parent = [i for i in range(n + 1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    x,y = find(a), find(b)
    parent[x] = y


for _ in range(m):
    tp,a,b = map(int,input().split())
    if tp == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")