import sys
from _collections import defaultdict
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n + 1)]

# i는  1 ~ n
for i in range(1,n + 1):

    t = list(map(int,input().split()))
    # j 0 ~ n - 1 -> +1 -> 1~ n
    # 자기 자신은 안됨.
    for j in range(n):
        if i == j + 1 or  t[j] == 0 :continue
        # 무방향 그래프
        graph[i].append(j + 1)
        graph[j + 1].append(i)


path = list(map(int,input().split()))

# path 의 원소들이 모두 한 집합내에있으면 가능하다.
parent = [i for i in range(n + 1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]
def union(a,b):
    x = find(a)
    y = find(b)
    if x < y:
        parent[x] = y
    else:
        parent[y] = x
# (1,2) (2,3) 
# parent  0 1 2 3 -> 0 2 2 3 -> 0 2 3 3 
#  
for i in range(1,n + 1):
    # 연결된 그래프라면 합쳐주기
    for j in graph[i]:
        union(i,j)
answer = set()
for i in range(len(path)):
    answer.add(find(path[i]))
if len(answer) == 1:
    print("YES")
else:
    print("NO")
