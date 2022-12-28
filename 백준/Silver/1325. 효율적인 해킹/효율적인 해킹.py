import sys
from _collections import defaultdict,deque
input = sys.stdin.readline

n,m = map(int,input().split())

# a -> b 를 신뢰한다
# 다시말하면 b 를 해킹하면 a 를 해킹할수 있다.
# 하지만 root 를 모름?
# 서로 신뢰하는 경우도 있음
tree = defaultdict(list)

for _ in range(m):
    a,b = map(int,input().split())
    tree[b].append(a)
# 1번수행할떄마다 시간복잡 O(N) 공간 O(M) 서로 신뢰하는경우, 다 연결되어있는 그래프일때
def bfs(i):
    visited = [0]*(n + 1)
    q = deque([i])
    cnt = 1
    visited[i] = 1
    while q:
        node= q.popleft()
        for adj in tree[node]:
            if not visited[adj]:
                visited[adj] = 1
                q.append(adj)
                cnt += 1
    return cnt
answer = defaultdict(list)
max_val = 0
for i in range(1, n + 1):
    #bfs 수행
    x = bfs(i)
    # 최댓값 갱신
    if x > max_val:
        max_val = x
    answer[x].append(i)
print(*answer[max_val])