import sys
input = sys.stdin.readline

m,n = map(int,input().split())
arr = list(map(int,input().split()))

sn,en = 1,max(arr)
ans = 0


while sn <= en :
    mid = (sn + en) // 2
    cnt = 0
    for i,v in enumerate(arr):
        cnt += v // mid


    if cnt >= m:
        ans = mid
        sn = mid + 1
    else:
        en = mid - 1
print(ans)
