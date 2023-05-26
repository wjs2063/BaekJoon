import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))

counter_a = Counter(a)

ans = [-1] * n
stack = []

for i,v in enumerate(a):

    while stack and counter_a[stack[-1][0]] < counter_a[v] :
        val,idx = stack.pop()
        ans[idx] = v

    stack.append([v,i])
print(*ans)
