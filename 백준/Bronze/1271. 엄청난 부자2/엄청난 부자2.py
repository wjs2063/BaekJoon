import sys 
input = sys.stdin.readline 
n,m = map(int,input().split())
q,r = divmod(n,m)
print(q)
print(r)