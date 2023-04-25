def solution(a, b, n):
    tot = n 
    ans = 0 
    while tot >= a :
        x,r = divmod(tot,a)
        ans += b * x 
        tot = r + b * x 
        
    return ans