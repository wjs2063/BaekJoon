
import heapq
def solution(a):
    answer = 0
    n = len(a)
    # 양 끝점은 무조건 가능함 
    if n == 1 or n == 2:
        return n
    answer = 2
    # x번째 기준으로 좌 우의 최솟값이 둘다 나보다 작으면 불가능하다
    # 이걸 어떻게 효율적으로 찾아낼건가??
    # 나를기준으로 왼쪽 오른쪽 의 최솟값을 찾아야함 
    lm,rm = [int(1e11)]*len(a), [int(1e11)]*len(a)
    lm[0] = a[0]
    rm[n - 1] = a[n - 1]
    # 첫인덱스는 무조건 갱신될거라 오류 x
    # sliding and memozation
    
    # lm[i] := 0~ i 번째까지의 최소 값 
    # rm[i] := i ~ n - 1번쨰까지의 최솟값
    for i in range(1,len(a)):
        # 현재가 더 작으면 갱신해주기
        if a[i] < lm[i - 1]:
            lm[i] = a[i]
        else:
            # 이전값 그대로 갱신
            lm[i] = lm[i - 1]
    for i in range(n - 2, - 1, -1):
        if a[i] < rm[i + 1]:
            rm[i] = a[i]
        else:
            rm[i] = rm[i + 1]
    
    
    for i in range(1, len(a) - 1):
        if lm[i - 1] < a[i] > rm[i + 1]:
            continue
        answer += 1
                
    
    return answer