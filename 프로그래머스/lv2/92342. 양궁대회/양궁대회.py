def solution(n, info):
    # 이기는 경우 담기
    answer = []
    # state 11 자리 일텐데 00000111111 형식  1이면 이기고 0이면 진다
    # n 발을 쏜대, 질거면 확실히 지고 이길거면 무조건 1발만 더쏘자
    score = 0
    # 11자리가 필요함
    # 10000 00000 00 
    for state in range(1,1 << 12):
        lion,apeach = 0,0
        arrow = n
        sub = [0]*(11)
        for i in range(1,12):
            # 1이면 라이언이 이기는경우
            if state & ( 1 << i):
                lion += (i - 1)
                # apeach 보다 1발 더 쏴
                arrow -= info[-i] + 1
                sub[-i] = info[-i] + 1
            # 라이언이 지는경우 즉 어피치가 이기는 경우
            else:
                # 0발맞췄으면 apeach 도 점수획득 안돼
                if info[-i] == 0:
                    continue
                apeach += (i - 1)
        # apeach 가 이기는경우는 버려
        if apeach >= lion or arrow < 0  :
            continue
        # arrow 가 0이상이면??
        # 반복문 다돌고 왔는데 arrow 가 0 보다 작으면?? 무시
        # 남은경우는 그냥 0점에 몰빵 최하위 비트에 몰빵해서 주자
        # 0점에 몰빵
        sub[-1] += arrow
        # 최고기록이 현재점수보다 더 작으면 갱신
        answer.append([lion - apeach] + sub)
    
    if len(answer) == 0:
        return [-1]
    answer.sort(key = lambda x:(-x[0],-x[-1],-x[-2],-x[-3],-x[-4],-x[-5],-x[-6],-x[-7],-x[-8],-x[-9],-x[10],-x[-11]))
    return answer[0][1:]
    
    