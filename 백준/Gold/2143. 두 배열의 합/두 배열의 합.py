import sys
from _collections import defaultdict
input = sys.stdin.readline

t = int(input().strip())

n = int(input().strip())
a = [0] + list(map(int,input().split()))
m = int(input().strip())
b = [0] + list(map(int,input().split()))

h1 ,h2 = defaultdict(int),defaultdict(int)

for i in range(1,len(a)):
    a[i] += a[i - 1]
for i in range(1,len(b)):
    b[i] += b[i - 1]

for i in range(1,len(a)):
    for j in range(i,len(a)):
        # i ~ j 까지
        h1[a[j] - a[i - 1]] += 1

for i in range(1,len(b)):
    for j in range(i,len(b)):
        h2[b[j] - b[i - 1]] += 1
ans = 0
for x in h1:
    ans += h1[x] * h2[t - x]
print(ans)