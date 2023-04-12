def solution(sequence, k):
    ans = []
    n = len(sequence)
    s = 0
    l = 0
    for rdx,v in enumerate(sequence):
        s += v 
        while l < n and  s > k:
            s -= sequence[l]
            l += 1
        if s == k:
            ans.append([rdx - l + 1,l,rdx])
    ans.sort(key = lambda x:(x[0],x[1]))
    return ans[0][1:]
        
        
        