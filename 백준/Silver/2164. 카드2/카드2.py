import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

q = deque([i for i in range(1,n + 1)])

while len(q) != 1:
    # 제일위에있는 카드제거후
    q.popleft()
    q.append(q.popleft())

print(q[0])
