import sys
from collections import deque,defaultdict
input = sys.stdin.readline

def continuous(arr):
    if len(arr) == 0 :return []
    temp = []
    while arr:
        x = arr.popleft()
        temp.append(x)
        if arr and arr[0] != x + 1:
            return temp
    return temp
def bfs(root,arr):
    global tree
    global parent
    q = deque([root])

    while q:
        x = q.popleft()
        # level wise 로 돌면서
        if len(arr) == 0 :
            return
        temp = continuous(arr)
        tree[x].extend(temp)
        for t in temp:
            # t의 부모노드는 x 임
            parent[t] = x
            q.append(t)

while True:
    n,k = map(int,input().split())
    if n == 0 and k == 0: break
    arr = deque(map(int,input().split()))
    # 연속된 숫자들을 한 뭉치로 보자
    # tree[x] := x라는 노드의 자식노드들
    tree = defaultdict(list)
    # parent[i] : i노드의 부모노드
    parent = defaultdict(int)
    root = arr.popleft()
    # root 의 부모는 -1
    parent[root] = -1
    # -1 의 자식은 root
    tree[-1] = [root]
    # k노드의 부모노드를 찾은다음 len(tree[parent]) -> k노드가포함된 애들의 개수
    # 첫 root
    bfs(root,arr)
    # k 의 레벨을 찾고, 그 레벨의 개수에서 k라는 노드의 개수
    grand_father = parent[parent[k]]
    ans = 0
    for father in tree[grand_father]:
        if father == parent[k] : continue
        ans += len(tree[father])
    print(ans)



