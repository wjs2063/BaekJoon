import sys
from collections import deque
input = sys.stdin.readline

a,b = map(int,input().split())


def bfs():
    q = deque([(a,0)])
    visit = set()
    visit.add(a)
    while q:
        x,cnt = q.popleft()
        if x == b:
            return cnt + 1
        y = 2*x
        if y <= b and y not in visit:
            visit.add(y)
            q.append((y,cnt + 1))
        x = int(str(x) + "1")
        if x <= b and x not in visit:
            visit.add(x)
            q.append((x,cnt + 1))
    return -1
print(bfs())