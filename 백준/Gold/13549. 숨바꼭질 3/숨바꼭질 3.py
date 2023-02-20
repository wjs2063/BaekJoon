import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
def bfs(n,k):
    visit = set()
    q = deque([(n,0)])
    # 왼쪽으로 가야한다면 - 1 하는경우가 제일 빠르다
    visit.add(n)
    while q:
        pos,cnt = q.popleft()
        if pos == k:return cnt
        # x + 1과
        if pos <= 200000 and 2*pos not in visit:
            visit.add(2 * pos)
            q.appendleft((2 * pos,cnt))
        if pos + 1 not in visit:
            visit.add(pos + 1)
            q.append((pos + 1,cnt + 1))
        if pos - 1 >= 0 and pos - 1 not in visit:
            visit.add((pos - 1))
            q.append((pos - 1,cnt + 1))

        # x - 1 과
        # 2x 를보자

print(bfs(n,k))