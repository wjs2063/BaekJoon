import sys
input = sys.stdin.readline

a,b = map(int,input().split())

c = [0]*(max(a,b) + 1)

cnt = max(a,b)
x = 0
idx = 1
while cnt > 0 :

    for i in range(x):
        if cnt <= 0 :break
        c[idx] = x
        idx += 1
        cnt -= 1
    x += 1

for i in range(1,max(a,b) + 1):
    c[i] += c[i - 1]
print(c[b] - c[a - 1])