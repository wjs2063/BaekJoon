from collections import defaultdict,Counter
def solution(topping):
    # i번쨰 와 
    answer = 0
    left = defaultdict(int)
    right = Counter(topping)
    l_set,r_set = set(),set(topping)
    n = len(topping)
    # 0 ~ i번째까지 left 에 담기고 i + 1 부터 n - 1 까지 right 이라고보자
    for i,v in enumerate(topping):
        # i번쨰 원소를 left 에 추가, i번쨰원소를 right 에서 제거 
        l_set.add(v)
        right[v] -= 1
        if right[v] == 0:
            r_set.discard(v)
        if len(l_set) == len(r_set) :
            answer += 1
        
        
        
        
    
    
    return answer