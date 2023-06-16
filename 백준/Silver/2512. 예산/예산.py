import sys
input = sys.stdin.readline
n = int(input())

regions = list(map(int,input().split()))

tot = int(input())

ans = int(1e10)
m = max(regions)

sn,en = 0,tot

while sn <= en :
    # 지역의 상한 금액
    mid = (sn + en) // 2
    temp = 0
    val = 0
    for i,v in enumerate(regions):
        temp += min(v,mid)
        val = max(val,min(v,mid))
    # 총예산을 넘어가면 상한금액을 낮춰
    if temp > tot :
        en = mid - 1
    # 감당가능하면 갱신
    else:
        ans = val
        sn = mid + 1
print(ans)