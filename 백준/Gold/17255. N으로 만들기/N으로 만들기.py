import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = input().strip()

ans = 0
#현재 l <= x < r 의 string
visit = set()
def dfs(l,r,string,temp):
    # 종료조건
    if string == n and temp not in visit:
        global ans
        visit.add(temp)
        ans += 1
        return
    # 왼쪽을 먼저넣거나
    if l > 0 :
        dfs(l - 1,r,n[l - 1] + string,temp + string  )
    # 오른쪽을 먼저넣거나
    if r < len(n):
        dfs(l,r + 1,string + n[r],temp + string)

for i in range(len(n)):
    dfs(i,i + 1,n[i],"")
print(ans)
