import sys
from collections import deque
input = sys.stdin.readline

a,b,c = map(int,input().split())


def bfs(a,b,c):
    q = deque([(0,0,c)])
    visited = set()
    visited.add((0,0,c))

    while q:
        x,y,z = q.popleft()
        # a -> b 로 넣을수도
        if x != 0 :
            t = min(x,b - y)
            if (x - t,y + t,z) not in visited:
                visited.add((x - t,y + t , z))
                q.append((x - t,y + t,z))
            t = min(x,c - z)
            if (x - t,y,z + t) not in visited:
                visited.add((x - t,y, z + t))
                q.append((x - t,y,z + t))
        # a -> c 로 넣을수도
        # b -> c 로 넣을수도
        # b -> a 로 넣을수도
        if y != 0 :
            t = min(y,c - z)
            if (x,y - t, z + t) not in visited:
                visited.add((x,y - t,z + t))
                q.append((x,y - t, z + t))
            t = min(y,a - x)
            if (x + t,y - t,z) not in visited:
                visited.add((x + t,y - t,z))
                q.append((x + t,y - t,z))
        # c -> a 로 넣을수도
        if z != 0 :
            t = min(z,a - x)
            if (x + t,y, z - t) not in visited:
                visited.add((x + t,y, z - t))
                q.append((x + t,y, z - t))
        # c -> b 로 넣을수도
            t = min(z,b - y)
            if (x,y + t,z - t) not in visited:
                visited.add((x + t,y,z - t))
                q.append((x,y + t,z - t))
    return visited
temp = bfs(a,b,c)
ans = set()

for x in temp:
    if x[0] == 0:
        ans.add(x[2])
ans = sorted(list(ans))
print(*ans)
