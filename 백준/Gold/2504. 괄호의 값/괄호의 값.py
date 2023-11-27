import sys

input = sys.stdin.readline

vv = input().strip()
stack = []

ans = 0
temp = 1
val = 0

"""
열려있는 ( [ 에 대해서만 재귀를 진입하게된다.
"""
stack = []


def dfs(vv, idx, stack) -> (int, int):
    ans = 0
    while idx < len(vv):
        v = vv[idx]
        # ( or [ 라면
        if v == '(':
            # 값,진행된 인덱스
            stack.append(v)
            val, i = dfs(vv, idx + 1, stack)
            ans += 2 * val
            idx = i + 1
        elif v == '[':
            stack.append(v)
            val, i = dfs(vv, idx + 1, stack)
            ans += 3 * val
            idx = i + 1
        elif v == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                return (1, idx) if ans == 0 else (ans, idx)
            stack.append(v)
            idx += 1
        elif v == ']':
            if stack and stack[-1] == '[':
                stack.pop()
                return (1,idx) if ans == 0 else (ans, idx)
            stack.append(v)
            idx += 1
    return ans, idx


res, idx = dfs(vv, 0, stack)

if stack:
    print(0)
else:
    print(res)
