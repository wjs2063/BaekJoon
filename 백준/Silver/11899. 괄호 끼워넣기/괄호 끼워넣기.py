import sys
input = sys.stdin.readline

words = input().strip()

stack = []

for word in words:
    stack.append(word)
    # 1개씩 넣으면서 마지막 2개가 () 형식이면 제거
    while stack and stack[-2:] == ['(',')']:
        del stack[-2:]
# 남아있는 stack 의 길이만큼 쌍을 추가해야함
print(len(stack))
