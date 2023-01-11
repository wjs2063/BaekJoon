import sys
from collections import defaultdict
input = sys.stdin.readline

#
n = int(input().strip())
info = []
# 예제1번
# 1층에 B , B의 자식 2층에 A
# 1층에 A , A의 자식 2층에 B , B의자식 3층에 C , C의 자식 4층에 D
# 1층에 A , A의 자식 2층에 C ,
# 층수에 대한 정보와 부모에대한 정보가 필요하다
tree = defaultdict(list)
# 정렬해주고
for _ in range(n):
    xx = input()[2:]
    info.append(xx)
#소팅 해주기
info.sort()
for i in range(len(info)):
    info[i] = info[i].split()
ix = 0
# prev 에는 root 노드가 달라졌는지 체크
for i,x in enumerate(info):
    ix = 0
    # 이전것과 현재경로가 어디까지 중복되었는지 체크해야한다. 아니면 출력초과뜸
    if i - 1 >= 0:
        for j in range(len(x)):
            if info[i - 1][j] != x[j] or len(info[i - 1]) <= j:
                break
            ix += 1
    for j in range(ix,len(x)):
        print("--" * j + x[j])