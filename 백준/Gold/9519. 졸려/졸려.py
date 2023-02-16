import sys
input = sys.stdin.readline

x = int(input().strip())

w = input().strip()


def find_cycle(w):
    past = set()
    past.add(w)
    # 돌아가면서
    answer = [w]
    w = list(w)
    # abcde -> aebdc -> 그려보면 a b c 사이에 de 가 거꾸로들어감 ed 로
    while True:
        temp = ""
        front = w[:len(w) // 2 + 1]
        back = w[len(w) // 2 + 1:]
        while back:
            temp += front.pop(0)
            temp += back.pop()
        temp += "".join(front)
        #print(temp)
        if temp in past:
            break
        past.add(temp)
        answer.append(temp)
        w = list(temp)
    return answer
t = find_cycle(w)

x = x % len(t)

print(t[-x])
