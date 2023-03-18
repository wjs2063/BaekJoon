import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

# hanoi 함수 arr 배열을 src 에서 sub 를 거쳐 des 로 옮긴다
# 큰원판이 아래에
ans = 0
# 정답 출력 배열
s = []
def hanoi(left,right,l_pos,r_pos,des):
    """
    현재 arr 에는 무작위로 되어있다. 따라서 먼저 제일 큰 원판을 뺴내야함
    """
    if len(left) + len(right) < 1:
        return
    global ans,s
    # left,right 이 둘다 존재하면
    if left and right :
        # 둘중 최댓값이 어디있는지 체크해보자
        l,r = max(left),max(right)
        if l > r:
            idx = left.index(l)
            # 윗부분을 다 옮겨줘야한다
            for x in left[idx + 1:]:
                s.append([l_pos,r_pos])
            right += left[idx + 1:][::-1]
            # 그리고 제일큰 걸 옮기고
            s.append([l_pos,des])
            # 다시 재귀적인 하노이 수행
            hanoi(left[:idx],right,l_pos,r_pos,des)
        else:
            idx = right.index(r)
            for x in right[idx + 1:]:
                s.append([r_pos,l_pos])
            left += right[idx + 1:][::-1]
            s.append([r_pos,des])
            hanoi(left,right[:idx],l_pos,r_pos,des)
    else:
        if left :
            idx = left.index(max(left))
            # 윗 부분을 옮기고 다시 재귀
            for x in left[idx + 1:]:
                s.append([l_pos,r_pos])
            s.append([l_pos,des])
            right += left[idx + 1:][::-1]
            hanoi(left[:idx],right,l_pos,r_pos,des)
        else:
            idx = right.index(max(right))
            for x in right[idx + 1:]:
                s.append([r_pos,l_pos])
            s.append([r_pos,des])
            left += right[idx + 1:][::-1]
            hanoi(left,right[:idx],l_pos,r_pos,des)
hanoi(arr,[],1,2,3)
print(len(s))
for x in s:
    print(*x)
