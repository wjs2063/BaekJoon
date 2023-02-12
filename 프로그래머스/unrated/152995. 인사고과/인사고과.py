def solution(scores):
    answer = 0
    x,y = scores[0]
    s = x + y
    scores.sort(key = lambda x:(-x[0],x[1]))
    #내림차순,오름차순 정렬을 하게되면 
    # i < j 에 대하여 a[i][0] >= a[j][0] && a[i][1] <= a[j][1] 을 만족한다
    #첫번쨰 기준으로 정렬했으므로 그다음부터는 같거나 감소하는 방식으로 간다.
    
    prev = 0
    for i,v in enumerate(scores):
        if x < v[0] and y < v[1]:return -1
        if prev <= v[1]:
            if s < sum(v):
                answer += 1
            prev = v[1]
    return answer + 1