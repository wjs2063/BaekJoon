def solution(n, times):
    ans = 0
    sn,en = 1,max(times) * n 
    while sn <= en:
        # 최대 mid 시간
        mid = (sn + en) // 2
        # temp := mid 시간내에 검사할수있는 사람수
        temp = 0
        for i,v in enumerate(times):
            temp += mid // v
        # n명이상검사할수있다면 시간을 줄이고
        if temp >= n :
            ans = mid
            en = mid - 1
        # 검사못하면 시간을늘려야지
        else:
            sn = mid + 1
    return ans