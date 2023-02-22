import sys
from _collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

arr = []

while True:
    try :
        arr.append(int(input().strip()))
    except:
        break
tree = defaultdict(lambda :[-1,-1])
# reconfig sn 이상 en 미만 의 root 를 반환
def reconfig(sn,en):
    if sn >= en :
        return - 1
    boundary = en
    for i in range(sn + 1,en):
        if arr[i] > arr[sn]:
            boundary = i
            break
    tree[arr[sn]][0] = reconfig(sn + 1,boundary)
    tree[arr[sn]][1] = reconfig(boundary,en)
    return arr[sn]
reconfig(0,len(arr))

def dfs(root):
    if root == -1:
        return
    dfs(tree[root][0])
    dfs(tree[root][1])
    print(root)
dfs(arr[0])