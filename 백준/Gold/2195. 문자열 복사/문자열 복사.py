import sys
input = sys.stdin.readline

S = input().strip()
P = input().strip()

sub_set = set()

for i in range(len(S)):
    strs = ""
    for j in range(i,len(S)):
        strs += S[j]
        sub_set.add(strs)

l,r = 0,0
ans = 0

item = ""
while l < len(P):
    if r >= len(P):
        ans += 1
        break
    item += P[r]
    if item in sub_set :
        r += 1
    else:
        ans += 1
        item = ""
        l = r
print(ans)