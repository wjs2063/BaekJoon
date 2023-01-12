import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,m = map(int,input().split())

turns = []

for _ in range(m):
    a,b = map(int,input().split())
    if a > b:
        a,b = b ,a
    turns.append((a,b))

parent = [i for i in range(n)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    x,y = find(a),find(b)
    if x < y:
        parent[x] = y
    else:
        parent[y] = x
cnt = 1
for a,b in turns:
    # 사이클이있으면 종료
    if find(a) == find(b):
        break
    # 합쳐주자
    union(a,b)
    cnt += 1
if cnt > m :
    print(0)
else:print(cnt)
