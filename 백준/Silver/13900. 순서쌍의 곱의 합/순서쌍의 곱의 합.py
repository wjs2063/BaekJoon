import sys
input = sys.stdin.readline

n = int(input())

natural = list(map(int,input().split()))
num = natural[:]
# num[i] := i ~ 끝까지 합
for i in range(n - 2,-1,-1):
    num[i] += num[i + 1]
ans = 0

for i in range(n - 1):
    ans += natural[i] * num[i + 1]
print(ans)

