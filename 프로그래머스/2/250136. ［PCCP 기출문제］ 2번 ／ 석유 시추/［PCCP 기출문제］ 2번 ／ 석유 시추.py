from collections import deque,defaultdict
def bfs(land,vis,x,y,cnt,memo):
    n,m = len(land),len(land[0])
    q = deque([(x,y,1)])
    vis[x][y] = cnt
    memo[cnt] = 1
    while q:
        a,b,tot = q.popleft()
        for na,nb in [(a - 1,b),(a + 1,b),(a,b + 1),(a, b - 1)]:
            if not (0 <= na < n and 0 <= nb < m):continue
            if vis[na][nb]:continue 
            if land[na][nb] == 0 :continue
            memo[cnt] += 1
            vis[na][nb] = cnt 
            q.append((na,nb,tot + 1))

def solution(land):
    n,m = len(land),len(land[0])
    cnt = 0
    vis = [[0] * m for _ in range(n)]
    memo = defaultdict(int)
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and vis[i][j] == 0:
                cnt += 1
                bfs(land,vis,i,j,cnt,memo)
    answer = 0
    for c in range(m):
        temp = 0
        v = set()
        for r in range(n):
            if land[r][c] == 1 and vis[r][c] not in v:
                v.add(vis[r][c])
                temp += memo[vis[r][c]]
        answer = max(answer,temp)
    return answer