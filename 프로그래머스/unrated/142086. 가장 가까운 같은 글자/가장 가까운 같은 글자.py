def solution(s):
    from collections import defaultdict
    answer = []
    index_dict = defaultdict(lambda :-1)
    for i,v in enumerate(s):
        if index_dict[v] != -1 :
            answer.append(i - index_dict[v])
        else:
            answer.append(-1)
        index_dict[v] = i
    return answer