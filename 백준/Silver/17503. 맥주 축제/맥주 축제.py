import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

beer = []
mini,maxi = int(1e10),-1
for _ in range(k):
    v,c = map(int,input().split())
    mini = min(mini,c)
    maxi = max(maxi,c)
    beer.append([v,c])
# 선호도가 높은순으로 정렬
beer.sort(key = lambda x:-x[0])
#print(beer)
# beer[i] := i 번째 맥주의 선호도와, 도수

# 조건
# 1번. b1 + b2 + .. bn >= m
# 2번을 만족하게 하는 간레벨의 최솟값

# 이.탐 일까?
"""
상한을 정해놓고 가능한지 판단 ?
"""
INF = int(1e11)
sn,en = mini,maxi
ans = INF
while sn <= en :
    mid = (sn + en) // 2
    # 최대 mid만큼의 도수만 마실수있어
    temp,cnt = 0,0
    for i in range(k):
        v,c = beer[i]
        # n일 이상 마시면 끝
        if cnt >= n :break
        # 내주량초과면 패스하고
        if c > mid :continue
        temp += v
        cnt += 1
    # 선호도가 m 이상이면 가능하네?
    if temp >= m and cnt == n  :
        ans = mid
        en = mid - 1
    else:
        sn = mid + 1

if ans == INF :
    print(-1)
else:
    print(ans)