import sys 
input = sys.stdin.readline 

n,q = map(int,input().split())

seen = set()
for _ in range(q):
    node = int(input())
    root = node
    ans = 0
    while root:
        if root in seen : ans = root
        root //= 2
    if ans :
        print(ans)
    else:
        print(0)
        seen.add(node)
    
    