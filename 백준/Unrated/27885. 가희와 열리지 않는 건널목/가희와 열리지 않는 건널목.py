import sys
input = sys.stdin.readline

c,h = map(int,input().split())

tr = []

for _ in range(c):
    tr.append(input().strip())

for _ in range(h):
    tr.append(input().strip())
t = [0]*60*60*24


for time in tr:
    hour,minute,second = map(int,time.split(":"))
    start,end = second + 60*minute + 60*60*hour,second + 60*minute + 60*60*hour + 40
    t[start] += 1
    t[end] -= 1
ans = 0
for i,v in enumerate(t):
    if i >= 1:
        t[i] += t[i - 1]
    if t[i] == 0:
        ans += 1
print(ans)


