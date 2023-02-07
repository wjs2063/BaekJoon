import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
s = int(input())

for i,v in enumerate(arr):
    # 현재 위치에서 최대한 갈수있는 거리만봅시다
    mm = max(arr[i:min(n,i + s + 1)])
    idx = arr.index(mm)

    for k in range(idx,i,-1):
        arr[k], arr[k - 1] = arr[k - 1],arr[k]
    s -= (idx - i)
    if s == 0 :break
print(*arr)