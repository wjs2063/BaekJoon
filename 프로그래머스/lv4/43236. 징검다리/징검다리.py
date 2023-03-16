def solution(distance, rocks, n):
    ans = 0
    sn,en = 0,distance
    rocks = [0] + rocks
    # 최대 n 개의 바위를 없앨수있다.
    # 모든 바위의 간격이 mid 이상이게끔 만들수있냐
    rocks.sort()
    while sn <= en:
        mid = (sn + en) // 2
        # 각 지점사이 거리의 최솟값중에 가장 큰 값
        cnt = 0
        # 제거 돌의 개수 
        t = 0
        for i in range(len(rocks) - 1):
            cnt += abs(rocks[i] - rocks[i + 1])
            # 모든돌간의 거리가 mid 미만인게 있으면 안돼!
            if cnt < mid :
                t += 1
            else:
                cnt =0 
        if t > n:
            en = mid - 1
        else:
            ans = mid
            sn = mid + 1
        
                
    return ans