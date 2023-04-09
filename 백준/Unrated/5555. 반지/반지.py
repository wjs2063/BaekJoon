import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())

words = []

for _ in range(n):
    words.append(input().strip())
ans = 0

for word in words:
    if s in word*2:
        ans += 1
print(ans)