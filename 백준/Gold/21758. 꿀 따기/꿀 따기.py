import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

s = arr[:]

for i in range(1,n):
    s[i] += s[i - 1]

"""
벌 벌 꿀통
벌 꿀통 벌 
꿀통 벌 벌 
"""


a = 0
b = 0
c = 0
for i in range(1,n - 1):
    a = max(a,s[n - 1] - s[0] + s[n - 1] - s[i] - arr[i])
    b = max(b,s[n - 2] - s[i - 1] + s[i] - s[0])
    c = max(c,s[n - 2] + s[i - 1] - arr[i])


print(max(a,b,c))