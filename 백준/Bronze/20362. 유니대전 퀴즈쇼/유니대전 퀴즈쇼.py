import sys

input = sys.stdin.readline

n,first = input().split()
n = int(n)
cc = []
a = ""
for _ in range(n):
    name,ans = input().split()
    if name == first:
        a = ans
    cc.append([name,ans])
x = 0
for i,[name,ans] in enumerate(cc):
    if name == first:break
    if ans == a :
        x += 1
print(x)
