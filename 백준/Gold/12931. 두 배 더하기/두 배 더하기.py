import sys
input = sys.stdin.readline

n = int(input())
b = list(map(int,input().split()))
a = [0]*n
# 모든값이 0인 열 A

# A -> B 로만들기위한 연산의 최소횟수
# 1. 아무값중 1개를 + 1
# 2. 모든값을 2배

# 반대로 B -> A 로 만들자
# 100 -> 50 -> 25 -> 24 -> 12 -> 6 -> 3 -> 2 -> 1 -> 0 => 9번

# 2로 나누는게 제일 효율적임
# 홀수라면 짝수로만들어 -1 해주는작업이 필수임

def check(b):
    for i in range(n):
        if b[i] != 0:
            return True
    return False
answer = 0
while check(b):
    # 만약 홀수면 -1 해서 짝수만들어주고
    for i in range(n):
        if b[i] == 0:continue
        if b[i] % 2 == 1:
            answer += 1
            b[i] -= 1
    # 다 짝수면
    if check(b):
        answer += 1
        for i in range(n):
            b[i] //= 2

    # 나누기 2를해주고
print(answer)