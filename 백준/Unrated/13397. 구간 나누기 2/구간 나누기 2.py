import sys
input = sys.stdin.readline

n,m = map(int,input().split())

a = list(map(int,input().split()))


sn,en = 0,max(a) - min(a)
ans = 0
while sn <= en :
    # 구간점수의 최댓값 -> mid
    mid = (sn + en) // 2
    g = []
    cnt = 1
    mini,maxi = int(1e10),0
    for i,v in enumerate(a):
        mini = min(mini,v)
        maxi = max(maxi,v)
        g.append(v)
        if maxi - mini > mid :
            mini,maxi = v,v
            g = [v]
            cnt += 1
    if cnt > m:
        sn = mid + 1
    else:
        ans = mid
        en = mid - 1
print(ans)
