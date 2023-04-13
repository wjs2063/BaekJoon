def solution(targets):
    targets.sort(key = lambda x:x[1])
    idx = 0
    n = len(targets)
    ans = 0
    
    while idx < n :
        s,e = targets[idx]
        while idx < n and targets[idx][0] < e:
            idx += 1
        ans += 1
    
    return ans 
            