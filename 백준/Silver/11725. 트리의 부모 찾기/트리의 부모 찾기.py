import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().strip())

tree = defaultdict(list)

for _ in range(n - 1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
# 공간복잡도 O(N)
parent = [0]*(n + 1)
# parent[x] : x 번째 노드의 부모
# 1번을 루트라고 정함.
# 1번부터 bfs or dfs  순회하여 자식노드의 를 갱신
visited = [0]*( n + 1)
#부모노드는 방문처리
visited[1] = 1
# O(N)
def dfs(tree,root):
    global parent
    # 부모노드와 연결된 자식노드를 순회
    for child in tree[root]:
        #자식노드를 방문하지 않았다면
        if not visited[child]:
            #자식노드 방문처리하고 parent 에 갱신 다시 dfs
            visited[child] = 1
            parent[child] = root
            # 이번에는 child 가 root 가 됨
            dfs(tree,child)
    return
dfs(tree,1)
# O(N)
for i in range(2,n + 1):
    print(parent[i])

# 최종 시간복잡도 O(N)
# 최종 공간복잡도 O(N)