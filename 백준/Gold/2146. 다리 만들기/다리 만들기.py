import sys
from collections import deque,defaultdict
input = sys.stdin.readline

n = int(input().strip())

graph = []
out_bound = defaultdict(set)
for _ in range(n):
    graph.append(list(map(int,input().split())))

def bfs(s,cnt,out_bound):
    n = len(graph)
    x,y = s
    q = deque([(x,y)])
    visited[x][y] = 1
    graph[x][y] = cnt

    while q:
        x,y = q.popleft()
        for dx,dy in zip([-1,1,0,0],[0,0,-1,1]):
            nx = x + dx
            ny = y + dy
            # 범위
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] :continue
            # 외곽지역이란소리
            if graph[nx][ny] == 0:
                out_bound[cnt].add((x,y))
            else:
                q.append((nx,ny))
                graph[nx][ny] = cnt
                visited[nx][ny] = 1


ans = int(1e10)

cnt = 1
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and not visited[i][j]:
            bfs((i,j),cnt,out_bound)
            cnt += 1


# 대륙마다 다 번호가 메겨졌다.
# print(graph)
# 각 대륙끼리의 거리 계산을 해야하는데.
# dist[v] := v  섬이 v일때 다리길이의 최솟값
def bfs1(cnt):
    global ans
    n = len(graph)
    dist = [[-1]*n for _ in range(n)]
    q = deque([])
    # cnt 섬의 외곽지역을 다 넣어주고
    for ob in out_bound[cnt]:
        x,y = ob
        dist[x][y] = 0
        q.append(ob)
    while q:
        x,y = q.popleft()
        for dx,dy in zip([-1,1,0,0],[0,0,-1,1]):
            nx = x + dx
            ny = y + dy
            #범위 벗어나면 패스
            if nx < 0 or nx >= n or ny < 0 or ny >= n :continue
            # 바다인 지점이고 한번도 가보지않은 점이라면
            if graph[nx][ny] == 0 and dist[nx][ny] == -1 :
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
            # 바다가아니고  다른 섬을 만났으면
            if graph[nx][ny] != 0 and  graph[nx][ny] != cnt:
                ans = min(ans,dist[x][y])
                return 
    #print(dist)
for i in range(1,cnt):
    bfs1(i)
print(ans)

