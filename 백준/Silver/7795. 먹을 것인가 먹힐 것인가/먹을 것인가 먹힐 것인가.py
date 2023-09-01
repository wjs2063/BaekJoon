import sys
from _bisect import bisect_left
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    ans = 0
    for idx,a in enumerate(A):
        ans += bisect_left(B,a)
    print(ans)
