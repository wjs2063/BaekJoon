import sys
input = sys.stdin.readline

n,m = map(int,input().split())

tree = list(map(int,input().split()))

ans = 0

sn ,en = 0, max(tree)

# sn 이상 en 이하

while sn < en :
    mid = (sn + en ) // 2
    # 가지고갈수있는 나무 길이 := h
    h = 0
    # 가지고있는 나무
    for t in tree:
        if t > mid :
            h += t - mid
    if h >= m :
        sn = mid + 1
        ans = mid
    else:
        en = mid
print(ans)
