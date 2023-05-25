import sys
input = sys.stdin.readline

n,m = map(int,input().split())

snow = [1] + list(map(int,input().split()))

ans = 0

# idx 에 도착한 시점에 남은 time과 눈덩이 크기 res
def dfs(time,idx,res):
    global ans
    ans = max(ans,res)
    if time == 0 :
        return
    # 2칸 갈래
    if idx + 2 <= n :
        dfs(time - 1,idx + 2,res // 2 + snow[idx + 2])
    if idx + 1 <= n :
        dfs(time - 1,idx + 1,res + snow[idx + 1])

    # 1칸 갈래


dfs(m,0,1)

print(ans)

