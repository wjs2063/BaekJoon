def solution(plans):
    ans = []
    for i,[name,start,playTime] in enumerate(plans):
        h,m = map(int,start.split(":"))
        plans[i][1] = 60 * h + m 
        plans[i][2] = int(playTime)
    plans.sort(key = lambda x:x[1])
    rest = []
    
    endTime = 0
    for i,[name,start,playTime] in enumerate(plans):
        # 이전과제의 종료시점이 현재과제보다 이전에끝나면 추가
        if i and endTime <= start:
            ans.append(subject)
        # 하던 과제를 멈추고 i 번째에있는 과제를 진행해야하는경우
        if endTime > start :
            rest.append([subject,endTime - start])
            
        # 시간이 남아돌아 이전에 하던 과제를 할수있는 경우
        else :
            while rest:
                sbj,time = rest.pop()
                if endTime + time <= start:
                    endTime += time
                    ans.append(sbj)
                else:
                    rest.append([sbj,endTime + time - start])
                    break
        # 이전 과제이름,끝나는시간
        subject = name
        endTime = start + playTime
    # 남은거 다넣어 
    rest.append([subject])
    while rest:
        ans.append(rest.pop()[0])
    return ans