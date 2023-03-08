import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(1,n):
    arr[i] += arr[i - 1]
# arr[x] := 0 ~ x 까지 누적합
ans = [arr[k - 1]]
for i in range(1,n - k + 1):
    ans.append(arr[i + k - 1] - arr[i - 1])
print(max(ans))