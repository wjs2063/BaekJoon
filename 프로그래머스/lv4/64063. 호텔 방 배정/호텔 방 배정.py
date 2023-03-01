from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
# x 의 부모 찾기
parent = defaultdict(int)
def find(x):
    if parent[x] == 0:
        parent[x] = x + 1
        return x
    else:
        parent[x] = find(parent[x])
    return parent[x]

def solution(k, room_number):
    answer = []
    for room in room_number:
        answer.append(find(room))
    return answer