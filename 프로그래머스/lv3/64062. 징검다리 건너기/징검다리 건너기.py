def solution(stones, k):
    ans = 0
    n = len(stones)
    sn ,en = min(stones),max(stones)
    # sn 이상 en 이하 까지 검사
    while sn <= en :
        mid = (sn + en) // 2
        # mid 명까지 지나갈수있다 , c
        cnt = 0
        flag = False
        for i in range(n):
            # mid 명이 가면 mid - 1 명까지 지나보내면 -> mid - 1 을 해준다음 생각
            if stones[i] - (mid - 1) <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k :
                flag = True
                break
        if flag:
            en = mid - 1
        else:
            ans = mid
            sn = mid + 1
    return ans