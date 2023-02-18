import sys
input = sys.stdin.readline

n = int(input().strip())

arr = []

tot_b = 0
for _ in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
    tot_b += b
ans = 0
for i in range(n):
    ans += arr[i][0]*(tot_b - arr[i][1])

print(ans)
