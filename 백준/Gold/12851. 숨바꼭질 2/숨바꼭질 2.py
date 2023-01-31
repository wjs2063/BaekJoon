import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

def bfs(n,k):
    # 시작지점 넣고
    q = deque([n])
    # 왔다갔다 반복하는 것 막기위해서  memozation 쓰기
    # 둘중 큰값 보다 2배이상갈일은없다
    t = 2*max(n,k) + 1
    INF = int(1e10)
    # visited[i] 에는 i까지 오는데 걸린 시간, i까지올수있는 가짓수 를 저장해보자
    visited = [[INF,-1] for _ in range(t)]
    visited[n] = [0,1]
    while q:
        x = q.popleft()
        for n_step in [x - 1,x + 1 ,2*x]:
            if 0 <= n_step < t :
                # 만약 처음방문하는곳이라면
                if visited[n_step][0] == INF:
                    # 이전에 걸린 시간 + 1 만큼 걸릴것이고
                    visited[n_step][0] = visited[x][0] + 1
                    # n_step 에서 까지올떄는 visited[x][1]만큼 걸림
                    visited[n_step][1] = visited[x][1]
                    # 처음방문할때는 1가지
                    q.append(n_step)
                # 만약에 이전에 방문했던경우면 다시 계산 필요 x
                elif visited[n_step][0] == visited[x][0] + 1:
                    visited[n_step][1] += visited[x][1]
    return visited


t = bfs(n,k)

print(t[k][0])
print(t[k][1])
