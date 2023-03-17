def solution(distance, rocks, n):
    ans = 0
    rocks = [0] + rocks
    rocks.sort()
    
    sn,en = 0,distance
    
    while sn <= en:
        mid = (sn + en) // 2
        cnt = 0
        t = 0
        for i in range(len(rocks) - 1):
            cnt += abs(rocks[i] - rocks[i + 1])
            # 돌제거
            if cnt < mid:
                t += 1
            else:
                cnt = 0
        if t > n:
            en = mid - 1
        else:
            ans = mid
            sn = mid + 1
            
                
        
    return ans