

        


def solution(info, edges):
    answer = 0
    # bit mask 
    visited = [0] * (1 << 17)
    n = len(info)
    # make tree 
    tree = [[-1,-1] for _ in range(n)]
    for p,c in edges:
        if tree[p][0] == -1: tree[p][0] = c
        else:tree[p][1] = c
        
    val = info
    def sol(state):
        nonlocal visited
        nonlocal answer
        nonlocal tree
        nonlocal val
        # 상태를 방문했었더라면?
        if visited[state] : return 
        # 방문체크
        visited[state] = 1
        wolf,num = 0,0
        # 양은 0 늑대는 1 
        for i in range(n):
            # 현재 상태의 늑대 수 구하기 -> 즉 현재 방문노드의 늑대 마리수 체크 (state & ( 1 << i))
            if state & (1 << i):
                num += 1
                wolf += val[i]
        # 정점 = 양의수 + 늑대수
        if 2*wolf >= num : return
        answer = max(answer, num - wolf)
        # next step
        for i in range(n):
            # 방문하지 않은곳이면 패스하고
            if not state & ( 1 << i): continue
            # 방문 한 곳이면 현재 노드를 방문체크하고 다음 스텝으로 넘겨
            if tree[i][0] != -1:
                sol(state | (1 << tree[i][0]))
            if tree[i][1] != -1:
                sol(state | ( 1 << tree[i][1]))
    sol(1)
            
                
        
    
    return answer