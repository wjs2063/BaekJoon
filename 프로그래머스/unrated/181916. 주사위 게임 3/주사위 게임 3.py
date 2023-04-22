def solution(a, b, c, d):
    res = 0
    from collections import Counter
    cc = Counter([a,b,c,d])
    s = list(set(cc.keys()))
    if len(s) == 1:
        res += 1111 * s[0]
    elif len(s) == 2 and cc[s[0]] == cc[s[1]] == 2 :
        res += (s[0] + s[1] ) * abs(s[0] - s[1])
    elif len(s) == 2 and (cc[s[0]] in [1,3] ):
        p,q = s[0],s[1]
        if cc[p] == 1:
            p,q = q,p
        res += (10 * p + q) ** 2
    elif len(s) == 3 :
        x = []
        for y in s:
            if cc[y] == 1:
                x.append(y)
        p,q = x 
        res += p * q
            
    else:
        res += min([a,b,c,d])
    return res