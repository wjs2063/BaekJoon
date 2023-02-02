import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())
temp = 1
def dfs(a,b,c):
    if b == 1:
        return a % c
    # b 가짝수
    if b % 2 == 0:
        return (dfs(a,b // 2,c)**2) % c
    else:
        return ((dfs(a,b // 2 ,c)**2)*a) % c
# O(logN)
print(dfs(a,b,c))