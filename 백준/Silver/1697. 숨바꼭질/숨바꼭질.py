import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
def bfs(n,k):
    # 같은지점이면 0
    if n == k :return 0
    q = deque([n])
    time = [0]*(2*10**5 + 1)
    # time[x] := x 까지 오는데 걸리는 최단시간
    # bfs 로하는이유는 최단거리찾기위해서 먼저도착하면 바로종료
    while q:
        x = q.popleft()
        if x == k :
            return time[x]
        #방문한점 패스
        # x - 1지점
        if x - 1 >= 0 and x <= 2*10**5 and time[x - 1] == 0:
            time[x - 1] = time[x] + 1
            q.append(x - 1)
        # 처음 도착하는곳이면
        if x + 1 <= 2*10**5 and time[x + 1] == 0:
            time[x + 1] = time[x] + 1
            q.append(x + 1)
        if 2*x <= 2*10**5 and time[2*x] == 0 :
            time[2*x] = time[x] + 1
            q.append(2*x)
    return time[k]
print(bfs(n,k))