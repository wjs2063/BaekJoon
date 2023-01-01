import sys
from collections import defaultdict,deque
input = sys.stdin.readline

n,m = map(int,input().split())

graph = defaultdict(list)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n + 1)
#연결요소 개수 담을 변수
cnt = 0


# O(N)
def bfs(i):
    global visited
    global graph
    q = deque([i])
    visited[i] = True
    while q :
        node = q.popleft()
        # node 와 연결된 모든 정점들을 돌면서
        for x in graph[node]:
            # 방문하지않았으면
            if not visited[x]:
                #방문체크하고 q에 추가
                visited[x] = True
                q.append(x)
    return None


for i in range(1,n + 1):
    if not visited[i]:
        cnt += 1
        bfs(i)
print(cnt)

# 시복,공복 모두 O(N)