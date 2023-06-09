import sys
input = sys.stdin.readline

n = int(input())

start = []
end = []


for _ in range(n):
    start.append(input().strip())
for _ in range(n):
    end.append(input().strip())

ans = 0

for i,v in enumerate(end):
    if v == start[i]:continue
    x = start.pop(start.index(v))
    start.insert(i,x)
    ans += 1


print(ans)