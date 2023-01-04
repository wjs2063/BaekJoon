import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input().strip())

conf = []

for _ in range(n):
    start,end,p = map(int,input().split())
    conf.append((start,end,p))

conf.sort(key = lambda x: (x[0],x[1]))

dp = [0]*n
# 가장 처음에 끝나는 회의
dp[0] = conf[0][2]
# dp[i] := 0 ~ i 번째 회의까지  참가가능한 사람의 최댓값



if n >= 2:
    dp[1] = conf[1][2]

for i in range(2,n):
    # i 보다 작은값들에 대해서 다 돌아 그래서 dp[i] 를 갱신
    for j in range(0,i - 1):
        # i - 2, i - 3 , i - 4  . . . 0 이유는 i번 회의는 i - 1회의랑 안겹친대
        dp[i] = max(dp[j] + conf[i][2],dp[i])
#여러 회의가 있을텐데 c1,c2,c3,c4 ~
print(max(dp))
