import sys
input = sys.stdin.readline

n = int(input().strip())

arr = list(map(int,input().split()))
for i,v in enumerate(arr):
    arr[i] = [v,i + 1]
x = 0
answer = []

while True:
    t = arr.pop(x)
    answer.append(t[1])
    if len(arr) == 0:
        break
    if t[0] > 0:
        t[0] -= 1
    x = (x + t[0]) % len(arr)




print(*answer)
