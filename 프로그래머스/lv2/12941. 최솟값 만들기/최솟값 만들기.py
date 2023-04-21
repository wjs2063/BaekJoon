def solution(A,B):
    res = 0
    A.sort()
    B.sort(reverse = True)
    
    for i,v in enumerate(A):
        res += v * B[i]
    res1 = 0
    A.sort(reverse = True)
    B.sort()
    
    for i,v in enumerate(A):
        res1 += v * B[i]
    
    return min(res,res1)