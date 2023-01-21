import sys
input = sys.stdin.readline

n = int(input().strip())

arr = list(map(int,input().split()))

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:return False
    return True
ans = 0
for x in arr:
    if is_prime(x):
        ans += 1
print(ans)