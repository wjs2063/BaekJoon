import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input().strip())



# 재귀적으로 계속 들어갔을떄 -> a -> b -> . . . -> a 로 오는경우만 팀

# a -> b -> c -> a 인데 만약 d -> a 이면 d 는 팀에끼지못한다.


# dfs := x 라는 노드의 choose가 이미 visited안에 있으면 사이클이 생긴것
# dfs 로 탐색하면서 이전에 탐색한 노드에 있는지 없는지 체크


def dfs(choose,visited,temp,x):
    # x번째 사람이 선택한 사람
    # 방문체크
    visited[x] = 1
    c = choose[x]
    temp.append(x)
    # c 를 이미 방문했으면?
    if visited[c]:
        # 현재 경로에 있는경우라면
        if c in temp:
            # 사이클 시작점부터
            return len(temp) - temp.index(c)
        return 0
    return dfs(choose,visited,temp,c)





for _ in range(t):
    n = int(input().strip())
    visited = [0]*(n + 1)
    choose = [0] + list(map(int,input().split()))
    team = 0
    # choose[x] := x 가 선택한 사람
    for i in range(1, n + 1):
        if visited[i]:continue
        # team 을 이뤘을떄는
        if i == choose[i]:
            visited[i] = 1
            team += 1
        else:
            k = dfs(choose,visited,[],i)
            team += k
    print(n - team)