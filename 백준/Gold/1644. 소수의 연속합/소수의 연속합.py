import sys
input = sys.stdin.readline

n = int(input().strip())

# 소수를 순서대로 정렬해서 prefix sum 을 만들고
# i ~ j 까지 합이 N 인경우 면 되지않냐?
# 투포인터? i ~ j 까지 합이 N

def get_prime(n):
    memo = [True]*(n + 1)
    memo[0],memo[1] = False,False
    for i in range(2,n + 1):
        if memo[i] :
            j = 2
            while (i * j ) <= n:
                memo[i*j] = False
                j += 1
    prime = []
    for i in range(n + 1):
        if memo[i]:
            prime.append(i)
    return prime
prime = get_prime(n)
en = 0
s = 0
ans = 0
for i in range(len(prime)):
    while en < len(prime) and s < n:
        s += prime[en]
        en += 1
    if s == n:
        ans += 1
    s -= prime[i]
print(ans)