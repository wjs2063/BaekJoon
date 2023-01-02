import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from _collections import defaultdict
n = int(input().strip())

# 1번섬에 도달할수있는 양의 최댓값
graph = defaultdict(list)
# sheep[i] := i번째 섬에 사는 양의수
# wolf[i] := i번째 섬에 사는 늑대 수
sheep = [0]*(n + 1)
wolf = [0]*(n + 1)
# graph[x] := x 번째 섬과 연결된 섬의 정보 (i번째섬,양 , 마리수)
for i in range(2, n + 1):
    t, a, adj = input().split()
    graph[int(adj)].append(i)
    if t == 'S':
        sheep[i] = int(a)
    else:
        wolf[i] = int(a)
answer = 0
# dfs 로 1번부터 역방향으로 순회
# dfs 의 sheep 매개변수 := vertex 까지 오면서 생존한 양의 수
# 늑대한마리는 최대 1마리만 잡아먹음 -> 1마리 잡아먹으면 다시는 안잡아먹음
# 각 vertex 에는 양이있거나 늑대가 있거나

# dfs 의미 : vertex 까지 올수있는 양의 수
def dfs(vertex):
    # vertex 까지 올수있는 양의 수
    ss = 0
    for adj in graph[vertex]:
        ss += dfs(adj)
    # vertex 에 양이있거나 늑대가있거나
    if sheep[vertex] > 0:
        #양추가
        ss += sheep[vertex]
        sheep[vertex] = 0
    # 늑대가있으면?
    elif wolf[vertex] > 0:
        # 늑대가 더많으면 반영후 0 반환
        if wolf[vertex] > ss :
            wolf[vertex] -= ss
            return 0
        ss -= wolf[vertex]
        wolf[vertex] = 0
    return ss
print(dfs(1))