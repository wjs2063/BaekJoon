import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

arr = []

# Two pointer + BFS
height = set()
for _ in range(n):
    x = list(map(int,input().split()))
    arr.append(x)
    for j in range(len(x)):
        #모든 height 를 집합으로 (중복제거)->
        height |= set(x)
#정렬해서
height = sorted(list(height))
mm = height[-1]
#거쳐간 수들중 최댓값과 최솟값의 차이
#bfs 돌면서 left <= 가는경로 <= right 인경로만 지나가는데
#그대신 min,max 기록하면서 left,right 을 지나간경우만 체크?
def bfs(left,right):
    # left,right -> 최저,최대지점을 정해놓고 시작
    n = len(arr)
    # 시작지점과 끝지점이 범위에 포함되지않으면 패스
    if not ( left <= arr[0][0] <= right ):return False
    if not ( left <= arr[n - 1][n - 1] <= right):return False
    visited = set((0,0))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([(0,0)])
    # 지나간 최대 최소 값을 기억하기
    mini,maxi = arr[0][0],arr[0][0]
    while q:
        x,y = q.popleft()
        #갱신
        # 도착지점도착했을때 ->  최저지점,최대지점을 지난경우에만 True
        if x == n - 1 and y == n - 1 :
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx,ny) in visited:continue
            # 범위에 해당하지 않으면 pass
            if not (left <= arr[nx][ny] <= right):continue
            visited.add((nx,ny))
            # 최대 최소 갱신해주고
            q.append((nx,ny))
    # 최종적으로 mini와 maxi가 같은지 체킹
    return False

# Initial value
ans = height[-1] - height[0]
for i in range(len(height)):
    #시작
    sn = height[i]
    # 최대지점 이분탐색으로 지정
    tt = sn
    en = mm
    # sn 이상 en 이하 로만 갈수있음
    while tt <= en:
        mid = (tt + en) // 2
        # sn 과 mid로 지나갈수있는경우 갱신
        if bfs(sn,mid):
            ans = min(ans,abs(mid - sn))
            en = mid - 1
        else:
            tt = mid + 1
print(ans)






