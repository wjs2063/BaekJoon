import sys
from collections import deque
input = sys.stdin.readline

a,b,c,d = map(int,input().split())


def bfs(a,b,c,d):
    q = deque([(0,0,0)])
    # 한물통을 물통 가득채우는 작업
    # 한물통을 모두 버리는 작업
    # A -> B or B -> A 작업
    visited = set()
    while q:
        A,B,cnt = q.popleft()
        if A == c and B == d:
            return cnt
        # A를 가득채우기
        if (a,B) not in visited:
            visited.add((a,B))
            q.append((a,B,cnt + 1))
        # B 가득채우기
        if (A,b) not in visited:
            visited.add((A,b))
            q.append((A,b,cnt + 1))
        # A물통버리기
        if (0,B) not in visited:
            visited.add((0,B))
            q.append((0,B,cnt + 1))
        # B 물통 버리기
        if (A,0) not in visited:
            visited.add((A,0,cnt + 1))
            q.append((A,0,cnt + 1))
        # A -> B 로 이동
        t = min(A, b - B)
        if (A - t, B + t) not in visited:
            visited.add((A - t, B + t))
            q.append((A - t,B + t,cnt + 1))
        # B -> A
        # t 의 의미는 A 로 부울수있는 만큼의 양을 측정
        t = min(B, a - A)
        if (A + t,B - t) not in visited:
            visited.add((A + t,B - t))
            q.append((A + t,B - t,cnt + 1))

        # B -> A 로 이동
    return - 1
print(bfs(a,b,c,d))