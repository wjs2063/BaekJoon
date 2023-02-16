import sys
input = sys.stdin.readline

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(int(input().strip()))

plus = []
minus = []
zero = 0
for x in arr:
    if x > 0:
        plus.append(x)
    elif x < 0:
        minus.append(x)
    else:
        zero = 1
# 포인트는 위치에 상관없이 묶는다는것이다
# 0 은 무시하자
# 그리디하게 곱이 높은애들만 묶자
plus.sort()
minus.sort(reverse = True)

answer = 0

while len(plus) >= 2:
    x,y = plus.pop(),plus.pop()
    answer += max(x * y,x + y)
if plus:
    answer += plus.pop()
while len(minus) >= 2:
    x,y = minus.pop(),minus.pop()
    answer += x * y
if minus:
    if not zero :
        answer += minus.pop()
print(answer)

