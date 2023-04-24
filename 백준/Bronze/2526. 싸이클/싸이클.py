import sys
input = sys.stdin.readline

n,p = map(int,input().split())

s = set()
arr = [n]
start = n
s.add(start)

while 1:
    x,r = divmod(start * n ,p)
    start = r
    if start in s :
        break
    arr.append(start)
    s.add(start)

print(len(arr) - arr.index(start))
