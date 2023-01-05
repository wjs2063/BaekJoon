import sys
sys.setrecursionlimit(10**6)
class TreeNode :
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
def config(arr):
    if len(arr) == 0:
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = config(arr[:mid])
    root.right = config(arr[mid + 1:])
    return root
# dfs 돌면서 값이 0인노드에 자식이없는지 확인 

    
        

def solution(numbers):
    answer = []
    # LVR 이잖아
    # 그러면 결국 numbers 에있는 넘버를 일단 이진수로 변환해서
    # 트리로 만들어 
    def dfs(root):
        nonlocal flag
        if root == None :
            return
        # 더미노드 밑에 0이아닌 더미노드가있으면?
        if root.val == '0' and (root.left or root.right):
            if root.left and root.left.val == '1':
                flag = False
                return
            if root.right and root.right.val == '1':
                flag = False
                return
                
        # 값이 0인데 자식노드가 존재한다? 불가능 (문제에서 원하는 더미노드가 아님)
        dfs(root.left)
        dfs(root.right)
        return None
    def full_bin(num):
        n = len(num)
        # 2^t - 1과 가장 가까운 수 찾아서 만들어줘야함 
        t = 1
        while 2**t <= n:
            t += 1
        return 2**t - 1 - n
        
            
    
    for num in numbers:
        num = bin(num)[2:]
        num = '0'*full_bin(num) + num
        # 포화이진트리 2*n - 1 개
        root = config(num)
        flag = True
        dfs(root)
        if flag:
            answer.append(1)
        else:answer.append(0)
        
        
    return answer