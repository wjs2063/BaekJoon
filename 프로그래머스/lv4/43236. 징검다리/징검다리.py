def solution(distance, rocks, n):
    ans = 0
    rocks.sort()
    sn,en = 1,distance
    # 모든 거리를 mid 이상 띄울수있냐?
    while sn <= en :
        mid = (sn + en) // 2
        
        dist = 0
        cnt = 0
        pos = 0
        for i in range(len(rocks) ):
            dist += rocks[i] - pos
            
            if dist < mid :
                cnt += 1
            else:
                dist = 0
            pos = rocks[i]
        if cnt <= n:
            ans = mid 
            sn = mid + 1
        else:
            en = mid - 1
                
    
    return ans