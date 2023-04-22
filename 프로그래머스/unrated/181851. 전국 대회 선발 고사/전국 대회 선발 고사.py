def solution(rank, attendance):
    answer = 0
    n = len(rank)
    s = []
    for i,v in enumerate(rank):
        if attendance[i] == True:
            s.append([v,i])
    s.sort()
    a,b,c = s[0][1],s[1][1],s[2][1]
    
    return 10000 * a + 100 * b  + c