def solution(n, s):
    answer = []
    if s // n <= 0: return [-1]
    answer = [s // n for _ in range(n)]
    if s % n == 0:
        return sorted(answer)
    for i in range(s % n):
        answer[i] += 1
    return sorted(answer)