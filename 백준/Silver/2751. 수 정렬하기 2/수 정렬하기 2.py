import sys
input = sys.stdin.readline

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
for x in arr:
    print(x)