import sys
from collections import defaultdict,deque
sys.setrecursionlimit(10**3)
input = sys.stdin.readline

n,m,v = map(int,input().split())
graph = defaultdict(list)
# 무방향 그래프
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# 소팅 Tim sort -> nlogn 보장
for i in range(1, n + 1):
    #정점이 작은 순서대로 정렬
    graph[i].sort()
# 총 n 개라고했을때 각각 소팅 a + b + c = n 일떄
# aloga + blogb + clogc <= nlogn ( 최악 1곳에 몰렸을때)

# recursive
# O(N)
def dfs(graph:list,v:int):
    # arr:= 정답배열
    arr = []
    visited = [0]*(1 << 10)
    stack = []
    def DFS(graph,visited,vt):
        nonlocal arr
        #방문체크
        visited[vt] = 1
        #정답배열에 추가
        arr.append(vt)
        for adj in graph[vt]:
            #방문하지 않았다면
            if not visited[adj]:
                #DFS 수행
                DFS(graph,visited,adj)
    # DFS
    DFS(graph,visited,v)
    print(*arr)



# O(N)
def bfs(graph : list,v : int):
    # arr := 정답출력배열
    arr = []
    # 방문체크 배열
    visited = [0]*(1 << 10)
    # queue
    q = deque([v])
    #방문체크 1은 방문 , 0은 방문x
    visited[v] = 1
    while q:
        x = q.popleft()
        arr.append(x)
        for adj in graph[x]:
            if not visited[adj]:
                q.append(adj)
                #방문 체크 미리
                visited[adj] = 1
    print(*arr)
    return None

# 최종 시간복잡도 O(MlogM + N) = O(MlogM)
# 최종 공간복잡도 O(M)
dfs(graph,v)
bfs(graph,v)