import sys
input = sys.stdin.readline 
n = int(input())
a = [0]*(10**4 + 1)
for _ in range(n):
    x = int(input())
    a[x] += 1
for i in range(10**4 + 1):
    if a[i] == 0 :continue
    while a[i]:
        print(i)
        a[i] -= 1

    