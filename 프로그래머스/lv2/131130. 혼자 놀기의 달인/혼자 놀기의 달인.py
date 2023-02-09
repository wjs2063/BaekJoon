def solution(cards):
    answer = 0
    
    def sol(i,cards):
        visit = set()
        x = cards[i]
        #첫번쨰상자 
        while x not in visit:
            visit.add(x)
            x = cards[x - 1]
        # 만약 1번만에 다 치웠으면 0 리턴
        if len(visit) == len(cards):
            return 0
        m = 0
        for i,v in enumerate(cards):
            if v in visit:continue
            second = set()
            while v not in visit and v not in second:
                second.add(v)
                v = cards[v - 1]
            m = max(m,len(second))
        return m * len(visit)
    for i,v in enumerate(cards):
        answer = max(answer,sol(i,cards))
        
    return answer