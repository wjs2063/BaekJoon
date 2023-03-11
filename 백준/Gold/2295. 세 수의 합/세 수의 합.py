import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse = True)
def solve(arr):
    sub_set = set()

    for i in range(n):
        for j in range(n):
            sub_set.add(arr[i] + arr[j])
    ans = []
    for i in range(n):
        for j in range(i + 1,n):
            if arr[i] - arr[j] in sub_set:
                ans.append(arr[i])
    return max(ans)
print(solve(arr))
