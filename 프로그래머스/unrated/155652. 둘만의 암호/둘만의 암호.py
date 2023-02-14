def solution(s, skip, index):
    answer = ''
    for x in s:
        x = ord(x) - ord("a")
        cnt = 0
        while cnt < index:
            x = (x + 1) % 26
            if chr(x + ord("a")) not in skip:
                cnt += 1
        answer += chr(x + ord("a"))
                
            
    return answer