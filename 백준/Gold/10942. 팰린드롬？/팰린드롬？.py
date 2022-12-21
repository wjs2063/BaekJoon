import sys
input = sys.stdin.readline
n = int(input().strip())
arr = list(map(int,input().split()))

dp = [[0]*n for _ in range(n)]
# 길이가 1 or 2 짜리 먼저 체크
for i in range(n):
    dp[i][i] = 1
    if i + 1 < n :
        if arr[i] == arr[i + 1]:
            dp[i][i + 1] = 1
# sn ~ en 까지 sn + 1 ~ en - 1 이 팰린드롬이고 sn번쨰와 en 번째가 같으면 팰린
# 길이가 1이거나
for i in range(n):
    for sn in range(n - i):
        en = sn + i
        if arr[sn] == arr[en] and en - sn  :
            if dp[sn + 1][en - 1] == 1:
                dp[sn][en] = 1
m = int(input().strip())
for _ in range(m):
    s,e = map(int,input().split())
    print(dp[s - 1][e - 1])
