def solution(A, B):
    answer = 0
    # O(NlogN)
    A.sort()
    B.sort()
    n = len(A)
    j = 0
    # B[j] 에 대하여 A[i] 보다 큰값을 찾아보자 
    for i in range(n):
        while j < n and A[i] >= B[j]:
            j += 1
        if j == n :
            break
        if A[i] < B[j]:
            j += 1
            answer += 1
            
    return answer