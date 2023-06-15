import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

grp = [[] for _ in range(n + 1)]

indegree = [0] * (n + 1)
ans = [0] * (n + 1)
for _ in range(m):
    a,b = map(int,input().split())
    grp[a].append(b)
    indegree[b] += 1

q = deque([])

for i in range(1,n + 1):
    if indegree[i] == 0 :
        q.append([i,1])

while q:
    cur_course,time = q.popleft()
    ans[cur_course] = time
    for next_course in grp[cur_course]:
        indegree[next_course] -= 1
        if indegree[next_course] == 0:
            q.append([next_course,time + 1])
print(*ans[1:])

