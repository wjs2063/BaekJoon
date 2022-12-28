import sys
from collections import defaultdict
input = sys.stdin.readline

# input 입력받기
n = int(input().strip())
m = int(input().strip())

# graph 정보 담을 2차원 배열
# graph[i] := i번쨰 vertex와 연결된 vertex
graph = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    # a 와 b 가 연결되어있다면, b와a 도 연결되어있음
    # 무방향 그래프
    graph[a].append(b)
    graph[b].append(a)
# ans := 정답 1번노드는 제외
ans = -1
# dfs 함수 : v와 연결된 모든 노드개수 파악
# 컴퓨터는 최대 100 개이므로 100 < 128
visited = [0]*( 1 << 7)
# dfs 시간복잡도 : O(N) 정점을 1번만 지남
def dfs(graph : list, v: int ) -> None:
    global ans
    if not graph[v] :
        return
    # 현재 노드 + 1
    ans += 1
    # 방문 체크
    visited[v] = 1
    for adj in graph[v]:
        if visited[adj]:continue
        dfs(graph,adj)
    return None
# dfs 순회
dfs(graph,1)
print(ans)
# 최종 시간복잡도 O(N) , 공간복잡도 O(N)