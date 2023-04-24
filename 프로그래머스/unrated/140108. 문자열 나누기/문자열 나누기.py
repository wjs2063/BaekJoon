import sys 
sys.setrecursionlimit(10**6)
def solution(s):
    res = 0 
    def dfs(strs):
        if strs == "":return 
        nonlocal res
        res += 1
        l,r = 0,0
        ff = strs[0]
        for i,v in enumerate(strs):
            if v == ff:
                l += 1
            else:
                r += 1
            if l == r :
                dfs(strs[i + 1:])
                break
    dfs(s)
    return res