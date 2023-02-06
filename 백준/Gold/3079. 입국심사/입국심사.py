import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(int(input().strip()))

sn,en = min(arr),m*max(arr)
ans = 0
while sn <= en:
    mid = (sn + en) // 2
    tot = 0
    # mid 시간으로 검사할수있는 사람수
    for i in range(n):
        tot += mid // arr[i]
    # 충분히 검사할수있으면 줄여
    if tot >= m :
        ans = mid
        en = mid - 1
    else:
        sn = mid + 1
print(ans)