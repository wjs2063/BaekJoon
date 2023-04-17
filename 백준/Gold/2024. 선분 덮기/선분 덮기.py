import sys
input = sys.stdin.readline

m = int(input())

lines = []

while True:
    l,r = map(int,input().split())
    if (l,r) == (0,0):break
    if l > r:
        l,r = r,l
    lines.append((l,r))
lines.sort(key = lambda x:(x[0],-x[1]))
# 0 <= x <= m 선분을 덮어야한다.
# 출발점은 짧고 끝점은 가장 큰것을 먼저보는게 이득이다

en = 0
ans = 0

"""
5일때 3,6 과 4 8 중 무엇을 선택해야하는가?
"""
n = len(lines)
idx = 0


while idx < n :
    l,r = lines[idx]
    # 현재덮은 선분보다 시작지점이 더 오른쪽에있으면 불가능해
    if en < l : break
    # 이미 덮혀진 경우면
    if r <= en :
        idx += 1
    else:
        t = en
        while idx < n and lines[idx][0] <= en:
            t = max(t,lines[idx][1])
            idx += 1
        en = t
        ans += 1
    if en >= m :break
if en < m :
    print(0)
else:
    print(ans)
