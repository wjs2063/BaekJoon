import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

arr = []
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for _ in range(n):
    arr.append(list(map(int,input().split())))

def bfs():
    q = deque([(0,0)])
    while q:
        x,y = q.popleft()
        if arr[x][y] == 0:continue
        t = arr[x][y]
        # t 만큼 갈수있다.
        if x + t < n :
            dp[x + t][y] += dp[x][y]
            q.append((x + t,y))
        if y + t < n:
            dp[x][y + t] += dp[x][y]
            q.append((x,y + t))
for i in range(n):
    for j in range(n):
        t = arr[i][j]
        if t == 0:continue
        if i + t < n:
            dp[i + t][j] += dp[i][j]
        if j + t < n:
            dp[i][j + t] += dp[i][j]

print(dp[-1][-1])