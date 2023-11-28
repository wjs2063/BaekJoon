import sys
input = sys.stdin.readline


n = int(input())

factor = list(map(int,input().split()))

MOD = int(1e9) + 7

factor.sort()

pow = [1]
for _ in range(n):
    pow.append((pow[-1] * 2) % MOD )
ans = 0
for i in range(1,n + 1):
    ans = (ans + (pow[i - 1] - pow[n - i]) * factor[i - 1]) % MOD

print(ans)
