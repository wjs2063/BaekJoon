import sys
input = sys.stdin.readline

n = int(input().strip())

arr = list(map(int,input().split()))

arr.sort()

l,r = 0,len(arr) - 1
ans = [[int(1e10),-1,-1]]
while l < r :
    temp = arr[l] + arr[r]

    if abs(temp) < ans[0][0]:
        ans[0] = [abs(temp),arr[l],arr[r]]
    # 산성이 쎈경우면 산성을줄이고
    if temp >= 0:
        r -= 1
    # 염기성이 쎈경우면 염기성을 줄여
    else:
        l += 1
print(*ans[0][1:])