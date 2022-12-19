import sys
input = sys.stdin.readline

class TreeNode:
    def __init__(self,val = 0, left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

def reconfig(VLR,LVR):
    if len(VLR) == 0 or len(LVR) == 0 :
        return None
    if len(VLR) == 0 :
        return TreeNode(VLR[0])
    root_val = VLR[0]
    idx = LVR.index(root_val)
    root = TreeNode(root_val)

    root.left = reconfig(VLR[1:idx + 1] , LVR[:idx])
    root.right = reconfig(VLR[idx + 1:], LVR[idx + 1:])
    return root

def dfs(root,x):
    if root == None:
        return
    dfs(root.left,x)
    dfs(root.right,x)
    x.append(str(root.val))
    return

while True:
    try:
        VLR,LVR = input().split()
        x = []
        root = reconfig(VLR,LVR)
        dfs(root,x)
        print("".join(x))
    except:
        break