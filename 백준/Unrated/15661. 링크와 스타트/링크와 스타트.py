import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

n = int(input())

a = []

for _ in range(n):
    a.append(list(map(int,input().split())))

tot = 0
for i in range(n):
    for j in range(n):
        tot += a[i][j]

s = [0]*n

for i in range(n):
    for j in range(n):
        s[i] += a[i][j] + a[j][i]

# i번째 사람이 가지는 영향력

ans = int(1e10)
def dfs(cnt,idx,temp):
    """
    :param cnt: cnt 는 팀의 개수 n - 1 이 넘어가면 안됨, 즉 최대 1:n - 1로 나뉘어야함
    :return:
    """
    if cnt >= n - 1 :return
    global ans
    ans = min(ans,abs(tot - temp))
    for i in range(idx,n):
        dfs(cnt + 1,i + 1,temp + s[i])
dfs(0,0,0)

print(ans)
