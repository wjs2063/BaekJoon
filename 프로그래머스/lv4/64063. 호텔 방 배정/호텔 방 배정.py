from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
# x 의 부모 찾기
parent = defaultdict(int)
# x번을 선택했을떄 배정할수있는 방
def find(x):
    # x번쨰방을 선택했을때 아무도 배정하지않은경우면
    if parent[x] == 0:
        # x번을 선택했을때 이제는 x + 1번째방을 배정해줄수있을것이고
        parent[x] = x + 1
        # 현재 배정해주는 x 를 return 해준다
        return x
    else:
        # 누군가가 배정이되었다면 
        # 거슬러 올라가서 예를들면 처음 5번방을 배정하려고하면 parent[5] = 6 이되고, 그다음 5번방을 또 배정하면
        # parent[5] = 
        parent[x] = find(parent[x])
    return parent[x]

def solution(k, room_number):
    answer = []
    for room in room_number:
        answer.append(find(room))
    return answer