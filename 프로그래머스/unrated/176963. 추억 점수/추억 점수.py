def solution(name, yearning, photo):
    from collections import defaultdict
    score = defaultdict(int)
    for a,b in zip(name,yearning):
        score[a] = b
    answer = []
    for person in photo:
        s = 0
        for p in person:
            s += score[p]
        answer.append(s)
            
    return answer