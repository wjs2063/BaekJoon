def solution(cards1, cards2, goal):
    # cards1 을 쓰거나 cards2를 쓰거나
    answer = 0
    def sol(idx1,idx2,temp):
        if len(temp) == len(goal):
            if temp == goal:
                nonlocal answer
                answer = 1
            return
        # card1 을 쓰는경우
        if idx1 < len(cards1) :
            sol(idx1 + 1,idx2,temp + [cards1[idx1]])
        if idx2 < len(cards2):
            sol(idx1,idx2 + 1,temp + [cards2[idx2]])
    sol(0,0,[])
    if answer :
        return "Yes"
    return "No"