def solution(r1, r2):
    answer = 0
    if r1 > r2:
        r1,r2 = r2,r1
    # r1 < r2 유지 
    # 원 위의점 포함해서 카운트 함
    def calculate1(radius):
        cnt = 0
        # x 축 ,y 축 위의 점
        cnt += 2 * (2 * radius + 1) - 1
        for i in range(1, radius):
            y = int((radius ** 2 - i ** 2)**0.5)
            cnt += 4 * y
        return cnt
    def calculate2(radius):
        cnt = 0
        cnt += 2 * (2 * radius + 1) - 1 - 4 
        for i in range(1, radius):
            y = int((radius ** 2 - i ** 2)**0.5)
            if y == (radius ** 2 - i ** 2)**0.5:
                y -= 1
            cnt += 4 * y
        return cnt
    pos2 = calculate1(r2)
    pos1 = calculate2(r1)
    print(pos1,pos2)
        
    
    return pos2 - pos1