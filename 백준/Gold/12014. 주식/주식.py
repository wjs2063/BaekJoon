import sys
from bisect import bisect_left
input = sys.stdin.readline

t = int(input())

for a in range(t):
    n,k = map(int,input().split())

    arr = list(map(int,input().split()))
    dp = [1]
    temp = [arr[0]]
    flag = False
    for i in range(len(arr)):
        if len(dp) == k:
            flag = True
            break
        if i == 0 :continue
        if temp[-1] < arr[i]:
            # 길이갱신
            temp.append(arr[i])
            dp.append(dp[-1] + 1)
        else:
            # 해당위치찾고
            idx = bisect_left(temp,arr[i])
            # 해당위치에 값넣어서 갱신
            temp[idx] = arr[i]
        if len(dp) == k:
            flag = True
            break
    print(f"Case #{a + 1}")
    if flag:
        print(1)
    else:
        print(0)
