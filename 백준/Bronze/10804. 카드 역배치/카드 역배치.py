import sys
input = sys.stdin.readline

card = [i for i in range(1,20 + 1)]

for _ in range(10):
    a,b = map(int,input().split())
    card[a - 1:b] = card[a - 1:b][::-1]
print(*card)