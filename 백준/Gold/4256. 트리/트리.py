import sys
input = sys.stdin.readline

t = int(input().strip())
class TreeNode :
    def __init__(self,val = 0 ,left = None, right = None):
        self.val = val
        self.left = None
        self.right = None
def reconfig_tree (vlr,lvr):
    if len(vlr) == 0 or len(lvr) == 0:
        return None
    if len(vlr) == 1:
        return TreeNode(vlr[0])
    # vlr 의 첫번쨰가 root
    root_val = vlr[0]
    node = TreeNode(root_val)
    # lvr 에서 root_val index 검색
    idx = lvr.index(root_val)
    # 인덱스 전후 로 나누기
    node.left = reconfig_tree(vlr[1:idx + 1],lvr[:idx])
    node.right = reconfig_tree(vlr[idx + 1:],lvr[idx + 1 :])

    return node
def dfs(root,x):
    if root == None:
        return
    dfs(root.left,x)
    dfs(root.right,x)
    x.append(root.val)


for _ in range(t):
    n = int(input().strip())
    vlr = list(map(int,input().split()))
    lvr = list(map(int,input().split()))
    root = reconfig_tree(vlr,lvr)
    x = []
    dfs(root,x)
    print(*x)