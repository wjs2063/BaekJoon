import sys
input = sys.stdin.readline

A = list(map(int,input().split()))
B = list(map(int,input().split()))
a = 0
b = 0
f = 0
for i,v in enumerate(A):
    a += A[i]
    if a > b:
        f = 1
        break
    b += B[i]



if f :
    print("Yes")
else:
    print("No")