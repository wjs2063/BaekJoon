def solution(info, edges):
    n = len(info)
    grp = [[] for _ in range(n)]
    for p,c in edges:
        grp[p].append(c)
    
    answer = 0
    seen = [0]*(1 << n)
    def dfs(state):
        nonlocal answer
        if seen[state] :return
        seen[state] = 1
        s,w = 0,0
        for i in range(n):
            if state & (1 << i):
                if info[i] == 0:
                    s += 1
                else:
                    w += 1
        if w >= s :return
        answer = max(answer,s)
        for i in range(n):
            if not state & ( 1 << i):continue
            for x in grp[i]:
                dfs(state | ( 1 << x))
    dfs(1)
        
    return answer