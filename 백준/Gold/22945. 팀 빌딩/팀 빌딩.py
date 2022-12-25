import sys

input = sys.stdin.readline
n = int(input().strip())

team = list(map(int,input().split()))

l,r = 0, n - 1
ans = 0
while l < r:
    ans = max(ans,(r - l - 1)*min(team[l],team[r]))
    if team[l] < team[r]:
        l += 1
    else:
        r -= 1
print(ans)