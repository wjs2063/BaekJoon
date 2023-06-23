import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

arr = [0]*(n + 1)

for i in range(1,n + 1):
    arr[i] = int(input().strip())

# 사이클 끼리만 합쳐서 정답내면된다.
ans = set()
def dfs(root,stack):
    up.add(root)
    if arr[root] in up:
        idx = stack.index(arr[root])
        global ans
        ans |= set(stack[idx:])
        return
    else:
        dfs(arr[root],stack + [arr[root]])

for i in range(1,n + 1):
    up = set()
    down = set()
    dfs(root = i,stack = [i])

print(len(ans))

for i,v in enumerate(sorted(list(ans))):
    print(v)

