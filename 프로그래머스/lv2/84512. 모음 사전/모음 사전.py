from itertools import product

def solution(word):
    answer = []
    for i in range(1,5 + 1):
        pp = product(["A","E","I","O","U"],repeat = i)
        pp = list(map("".join,pp))
        answer.extend(pp)
    answer.sort()
    
            
            
    return answer.index(word) + 1