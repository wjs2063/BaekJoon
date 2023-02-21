import sys
input = sys.stdin.readline

n,s = map(int,input().split())

arr = list(map(int,input().split()))
sub_sum = 0
l = 0
ans = float("inf")
for i,v in enumerate(arr):
    sub_sum += v
    # 부분합이 s 보다크면
    while sub_sum >= s :
        ans = min(ans,i - l + 1)
        sub_sum -= arr[l]
        l += 1
if ans == float("inf"):
    print(0)
else:
    print(ans)