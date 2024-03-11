import sys

si = sys.stdin.readline

strs = si().strip()
cnt_a = strs.count('a')
strs = 2 * strs
n = len(strs)
ans = int(1e10)
for i,v in enumerate(strs):
    if i + cnt_a - 1 < n :
        ans = min(ans,strs[i:i + cnt_a].count('b'))
print(ans)