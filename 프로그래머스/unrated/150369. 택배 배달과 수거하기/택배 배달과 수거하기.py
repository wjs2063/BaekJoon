def solution(cap, n, deliveries, pickups):
    res = 0
    d,p = 0,0
    for i in range(n - 1,-1,-1):
        d += deliveries[i]
        p += pickups[i]
        # 얼마나 왔다갔다해야함?
        c = 0 
        while d > 0 or p > 0 :
            d -= cap 
            p -= cap
            c += 1
        res += (i + 1) * 2 * c
            
        
    return res