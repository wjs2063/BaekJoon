import sys
from collections import deque
input = sys.stdin.readline


n,m = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))

# 기본 디폴트로 밑면과 윗면은 노출되어있음
# 가장자리는 옆면또한 노출되어있음 따로 계산
# bfs 를 돌면서
# 주변중에 큰것들과 비교하면서
# 가려지지않은 부분을 더해주자



ans = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    for j in range(m):
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if ni < 0 or ni >= n or nj < 0 or nj >= m :continue
            ans += max(0,arr[i][j] - arr[ni][nj])
# 윗면,아랫면은 무조건 노출이니 다 더해주고
ans += 2*n*m
# 가장자리 옆면은 무조건 노출되어있으므로  더해주자
for i in range(m):
    ans += arr[0][i]
    ans += arr[n - 1][i]
for i in range(n):
    ans += arr[i][0]
    ans += arr[i][m - 1]
print(ans)