def solution(k, d):
    ans = 0
    
    for x in range(0,d + 1,k):
        y = int((d ** 2 - x ** 2) ** 0.5)
        ans += y // k + 1
        
        
    return ans