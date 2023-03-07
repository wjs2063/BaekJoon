def solution(sequence):
    answer = 0
    n = len(sequence)
    
    dp1 = [sequence[i] * (-1) ** i for i in range(n)] 
    dp2 = [sequence[i] * (-1) ** (i + 1) for i in range(n)]
    seq1 = [sequence[i] * (-1) ** i for i in range(n)]
    seq2 = [sequence[i] * (-1) ** (i + 1) for i in range(n)]
    
    for i in range(n):
        if i >= 1:
            dp1[i] = max(dp1[i - 1] + seq1[i], seq1[i])
            dp2[i] = max(dp2[i - 1] + seq2[i], seq2[i])
    
    
    
    return max(max(dp1),max(dp2))