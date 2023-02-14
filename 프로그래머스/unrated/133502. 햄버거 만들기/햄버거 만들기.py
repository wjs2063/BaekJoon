def solution(ingredient):
    answer = 0
    stack = []
    for x in ingredient:
        stack.append(x)
        while len(stack) >= 4 and stack[-4:] == [1,2,3,1]:
            del stack[-4:]
            answer += 1
    return answer