import sys
input = sys.stdin.readline

n,m = map(int,input().split())

a = list(map(int,input().split()))
ans = int(1e10)
rc = []

sn = min(a);en = sum(a);

while sn <= en :
    mid = (sn + en) // 2
    # 1그룹당 최대 맥시멈 구슬값
    w = a[0]
    sub = 1
    info = [1]
    t = a[0]
    for i in range(1,len(a)):
        v = a[i]
        # 그룹을 하나 더만들어야함
        if w + v > mid :
            sub += 1
            w = v
            info.append(1)
        else:
            w += v
            info[-1] += 1
        t = max(t,w)

    if sub > m :
        sn = mid + 1
    else:
        ans = t
        rc = info
        en = mid - 1

print(ans)
print(*rc)
