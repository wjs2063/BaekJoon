from collections import defaultdict
vis = [0] * (1 << 17) # 상태 x 방문
def solution(info, edges):
    answer = 0
    n = len(info)
    # 0은 양, 늑대는 1 
    # info[x] : x 번째 노드에 들어있는 동물 
    # edges[i] = [부모노드,자식노드]
    tree = defaultdict(list)
    for p,c in edges:
        # 부모노드 ,자식노드
        tree[p].append(c)
    # root 노드는 항상 0
    def sol(state):
        if vis[state] :return
        vis[state] = 1
        w,s = 0,0
        # 현재 상태에서 얻은 양,늑대 개수를 카운트
        for i in range(n):
            if state & ( 1 << i):
                if info[i] == 0:
                    s += 1
                else:
                    w += 1
        if w >= s:return
        nonlocal answer
        answer = max(answer,s)
        for i in range(n):
            if not state & (1 << i):continue
            for x in tree[i]:
                sol(state | 1 << x)
    sol(1)
        
    return answer