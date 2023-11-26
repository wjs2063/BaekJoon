import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

a,b = map(int,input().split())

used = []
k = int(input())
for _ in range(k):
    used.append(int(input()))
# used[i] := 사용할 벽장의 번호


# 현재 a,b 가 열려ㅈ있는데
# X번째를 열어야한다면 -> abs(a - X ) 와 abs(b - X) 가 작은걸 먼저 열면된다.
# abs(a - X) 와 abs(b - X) 가 같다면 이제 둘중 무엇을 옮겨야할지 탐색해야한다. ( queue 에 넣고 갱신달리자)

res = int(1e10)

q = deque([(a,b,0,0)])
vis = set()
vis.add((a,b,0,0))
while q:
    a,b,cnt,tot = q.popleft()
    if cnt == k:
        res = min(res,tot)
        continue
    # a 가이동하는경우
    t = abs(a - used[cnt])
    # b 가이동하는경우
    y = abs(b - used[cnt])

    # a 가이동할지 체크
    # b 가이동할지 체크
    # a < b 는 유지된다.
    # a만 이동할수있는경우 사용해야할벽장이 < a
    # b 만이동할수있는경우 사용해야할벽장이 > b
    # 둘다이동가능한경우 a < 사용할벽장 < b

    if used[cnt] <= a :
        if (used[cnt], b, cnt + 1, tot + t) not in vis:
            vis.add((used[cnt], b, cnt + 1, tot + t))
            q.append((used[cnt], b, cnt + 1, tot + t))
    if used[cnt] >= b :
        if (a, used[cnt], cnt + 1, tot + y) not in vis:
            vis.add((a, used[cnt], cnt + 1, tot + y))
            q.append((a, used[cnt], cnt + 1, tot + y))
    if a < used[cnt] < b:
        if (used[cnt],b,cnt + 1,tot + t) not in vis:
            vis.add((used[cnt],b,cnt + 1,tot + t))
            q.append((used[cnt],b,cnt + 1,tot + t))
        if (a,used[cnt],cnt + 1,tot + y) not in vis:
            vis.add((a,used[cnt],cnt + 1,tot + y))
            q.append((a,used[cnt],cnt + 1,tot + y))
print(res)


