from collections import Counter
def count_1(a):
    a = bin(a)[2:]
    a = Counter(a)
    return a["1"]
    

def solution(n):
    answer = 0
    a = count_1(n)
    b = n + 1
    while True:
        x = count_1(b)
        if x == a:
            return b
        b += 1
    return 0