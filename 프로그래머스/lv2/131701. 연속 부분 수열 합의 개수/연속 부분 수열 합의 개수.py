def solution(elements):
    n = len(elements)
    elements.extend(elements)
    s = [0] + elements
    for i in range(1,len(s)):
        s[i] += s[i - 1]
    ans = set()
    for i in range(1,n + 1):
        for term in range(n):
            ans.add(s[i + term] - s[i - 1])
    return len(ans)
    
    