import sys
from _collections import deque
input = sys.stdin.readline

n = int(input().strip())
graph = []
start = []
tot = 0
min_heightofhouse = int(1e10)
max_heightofhouse = 0
height = set()
for i in range(n):
    graph.append(input().strip())
    for j in range(n):
        if graph[i][j] == "P":
            start.append((i,j))
        # 들러야할 집 개수
        if graph[i][j] == "K":
            tot += 1
# 정렬해서 한개씩늘려간다


tired = []
for i in range(n):
    tired.append(list(map(int,input().split())))
    # 들러야할 집들의 고도의 최솟값 저장
    height  |= set(tired[i])
    for j in range(n):
        if graph[i][j] == "K":
            min_heightofhouse = min(min_heightofhouse,tired[i][j])
            max_heightofhouse = max(max_heightofhouse,tired[i][j])
height = sorted(list(set(height)))


def bfs(start,k,left,right):
    # start ->
    x,y = start[0]
    n = len(graph)
    q = deque([(x,y)])
    # 만약 우체국고도가 해당되지않으면 패스
    if not (left <= tired[x][y] <= right):return False
    #상하좌우 대각선
    dirs = []

    for i in range(-1,1 + 1):
        for j in range(-1, 1 + 1):
            if i == 0 and j == 0 :continue
            dirs.append((i,j))

    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    cnt = 0
    # dirs 는 됐고  중복방문은 어떻게 처리할건데 ?/.. ㅎㄴㅎㅇㅎㅇㅁㄹㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴ.ㄹ.ㄴㅎ.ㅇㅁ.ㅇㅁ.ㄴㅁ
    # 최저 , 최대  차이가 무조건 MID 이내 여야한다...
    # MID 이내인것들중에서 왔다갔다 할수도있다. 기준을어떻게?..
    # BFS나 DFS 에서는 중복방문이 가능하기때문에 이를 제거해줄 수단이 필요하다 그게 기본적으로 visited 이다.
    # 근데 중복방문이 가능한경우라면 다른 기준이 필요하다.
    # 이문제에서는 최저고도 최고고도를 설정하여 진행하는것이 맞다.
    while q :
        x,y = q.popleft()
        for dx,dy in dirs:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == 1:continue
            # 갈수있는 고도 범위면
            if left <= tired[nx][ny] <= right:
                # 들리지않은 집이라면
                if graph[nx][ny] == "K":
                    cnt += 1
                visited[nx][ny] = 1
                q.append((nx,ny))
    return cnt == k

answer = int(1e10)

for i in range(len(height)):
    l = height[i]
    if l > min_heightofhouse: break
    # 불가능함 어차피 집은ㄷ ㅏ들려야하기때문에
    left = max_heightofhouse
    # 들러야할 집들중 제일 높은고도 와, 가장 높은 고도중 이분탐색 ( 집을 들리러가던과정중 필수불가결하게 높은곳을 들러야 하는 경우가있다)
    right = height[-1]
    temp = int(1e10)
    while left <= right:
        mid = (left + right) // 2
        rr = bfs(start,tot,l,mid)
        # 현재 고도로 가능하면 더 줄여보고
        if rr :
            temp = mid
            right = mid - 1
        else:
            left = mid + 1
    answer = min(answer,temp - l)
print(answer)


# 수평 수직 대각선 이동

# P -> 모든집돌고 -> 다시 P  갈때만 계산하면 올때는 그대로 내려오면 된다.

# x 피로도로 P -> 모든집 -> 다시 P 로 올수있는가 ?

# 피로도의 법위는 0 부터 1e6까지



