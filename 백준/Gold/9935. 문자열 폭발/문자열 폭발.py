import sys
input = sys.stdin.readline

stack = []

# stack에 하나씩넣으면서 문자열 있으면 계속 지워주기

s = input().strip()

exp_str = list(input().strip())

# O(NM)
for i in range(len(s)):
    stack.append(s[i])
    while len(stack) >= len(exp_str)  and stack[-len(exp_str):] == exp_str:
        del stack[-len(exp_str):]


if stack:
    print("".join(stack))
else:
    print("FRULA")