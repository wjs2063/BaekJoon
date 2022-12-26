import sys
input = sys.stdin.readline
from _collections import defaultdict
k = int(input().strip())

tree = list(map(int,input().split()))

mm = defaultdict(list)

def level_wise(tree,level):
    global mm
    n = len(tree)
    if n == 0:
        return
    mid = n // 2
    level_wise(tree[:mid],level + 1)
    mm[level].append(tree[mid])
    level_wise(tree[mid + 1:],level + 1)
level_wise(tree,0)

for i in range(k):
    print(*mm[i])