from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    d = defaultdict(int)
    for x,y in zip(want,number):
        d[x] += y
    temp = defaultdict(int)
    ss = sum(number)
    if len(discount) < ss :
        return 0
    for i in range(ss - 1):
        temp[discount[i]] += 1
    for i in range(len(discount) - ss + 1):
        temp[discount[i + ss - 1]] += 1
        if temp == d:
            answer += 1
        temp[discount[i]] -= 1
        if temp[discount[i]] == 0:
            del temp[discount[i]]
        

    return answer