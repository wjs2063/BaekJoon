def solution(targets):
    """
    targets.sort(key = lambda x:x[1])
    idx = 0
    n = len(targets)
    ans = 0
    
    while idx < n :
        s,e = targets[idx]
        while idx < n and targets[idx][0] < e:
            idx += 1
        ans += 1
    """
    ans = 0
    line = []
    for idx,(s,e) in enumerate(targets):
        line.append([s,e,idx,0])
        line.append([e,s,idx,1])
    line.sort()
    s = set()
    for i,v in enumerate(line):
        sn,en,idx,op = v 
        if op == 0:
            s.add(idx)
        elif op == 1:
            if idx in s:
                ans += 1
                s.clear()
                
        
    
    return ans 
            