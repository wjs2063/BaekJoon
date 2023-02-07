import math
from collections import deque
def solution(storey):
    answer = 0
    #현재 층에서 
    q = deque([(storey,0)])
    while q:
        x,cnt = q.popleft()
        if x == 0:
            return cnt 
        tt = int(math.log10(x))
        a,b = x - 10**tt, 10**(tt + 1 ) - x
        if a <= b:
            q.append((a,cnt + 1))
        else:
            q.append((b,cnt + 1))
    return answer