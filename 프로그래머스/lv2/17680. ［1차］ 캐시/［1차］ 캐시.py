def solution(cacheSize, cities):
    answer = 0
    c = []
    
    for city in cities:
        city = city.lower()
        # 현재 값이 cache 에있어?
        if city in c:
            answer += 1
            x = c.pop(c.index(city))
            c.append(x)
        else:
            answer += 5
            c.append(city)
            if len(c) > cacheSize:
                c.pop(0)
        
            
    
    return answer