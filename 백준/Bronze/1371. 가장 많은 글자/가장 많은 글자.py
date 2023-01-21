import sys
from collections import defaultdict
input = sys.stdin.readline
ans = defaultdict(int)
while True:
    x = input()
    if x == "":break
    xx = x.split()
    for x in xx:
        for t in x:
            ans[t] += 1
mm = max(ans.values())
res = []
for x in ans :
    if ans[x] == mm:
        res.append(x)
res.sort()
ans = ""
for x in res:
    ans += x
print(ans)