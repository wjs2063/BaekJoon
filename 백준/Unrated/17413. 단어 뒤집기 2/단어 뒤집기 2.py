import sys
input = sys.stdin.readline
strs = input()
temp = ""
ans = ""
for i,v in enumerate(strs):
    if v == ">":
        ans += temp + v
        temp = ""
    elif v == "<":
        xx = temp.split()
        for i,t in enumerate(xx):
            xx[i] = t[::-1]
        ans += " ".join(xx)
        temp = v
    else:
        temp += v
xx = temp.split()
for i,t in enumerate(xx):
    xx[i] = t[::-1]
ans += " ".join(xx)
print(ans)



