def solution(n):
    ans = ''
    while n :
        q,r = divmod(n,3)
        if r == 0 :
            ans += str(3)
            n = q - 1
        else:
            ans += str(r)
            n = q 
    ans = ans[::-1]
    ans = ans.replace("3","4")
            
    return ans