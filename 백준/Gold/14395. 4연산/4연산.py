import sys
from _collections import deque

si = sys.stdin.readline

s, t = map(int, si().strip().split())


def bfs(s, t):
    if s == t: return 0

    """
    s < t , 1부터시작하는경우와 s 에서부터 시작하는 경우 둘다  
    s == t 
    s > t ,1 부터 시작하는 경우와 2배, 제곱해서 갈수있는경우 1,2,4,8,16
    
    """
    ans = []

    q = deque([])
    vis = {s}
    q.append((s, ""))
    while q:
        integer, operators = q.popleft()
        if integer == t:
            ans.append(operators)
            continue
        if integer ** 2 <= int(1e9) and integer ** 2 not in vis:
            vis.add(integer ** 2)
            q.append((integer ** 2, operators + "*"))
        if 2 * integer <= int(1e9) and 2 * integer not in vis:
            vis.add(integer * 2)
            q.append((integer * 2, operators + "+"))
        if 1 not in vis:
            vis.add(1)
            q.append((1, operators + '/'))

    ans.sort(key=lambda x: (len(x), x))
    #print(ans)
    if not ans: return -1
    return ans[0]


print(bfs(s, t))
