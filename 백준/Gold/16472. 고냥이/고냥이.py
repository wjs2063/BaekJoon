import sys

si = sys.stdin.readline

# 인식할수있는 알파벳종류의 최대 개수
n = int(si().strip())
# 문자열
strs = si().strip()

memo = dict()

ans = 0
# Two Pointer
l, r = 0, 0


def add_alphabet(memo, alpha):
    if memo.get(alpha) is None:
        memo[alpha] = 1
    else:
        memo[alpha] += 1


def remove_alphabet(memo, alpha):
    memo[alpha] -= 1
    if memo[alpha] == 0:
        del memo[alpha]


while r < len(strs):
    # 현재 종류가 n 개보다 작다면 무조건 r 증가
    if len(memo) < n:
        add_alphabet(memo, strs[r])
        # 매번 갱신
        ans = max(ans,r - l + 1)
        r += 1
    # n개 일때 n개보다많을때
    else:
        # 현재 index에 알파벳이 memo의 key에 존재할때
        if memo.get(strs[r]) is not None:
            add_alphabet(memo, strs[r])
            ans = max(ans, r - l + 1)
            r += 1
        else:
            remove_alphabet(memo, strs[l])
            l += 1

        # 존재하지않을떄
print(ans)
