import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input().strip())
# 부모정보를 담을 배열 parent[i] := i번쨰의 부모
parent = [i for i in range(10**6 + 1)]
# a 의 부모찾기
# O(a(n)) a(n) 아커만 함수 : 2*65536 일때 5정도 값을 가짐
def find(parent,a):
    # 부모가 다르면
    if parent[a] != a :
        parent[a] = find(parent,parent[a])
    return parent[a]

def union(parent,a,b):
    # a 의 부모와 b 의 부모
    a = find(parent,a)
    b = find(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b
    return None

robot = [1]*(10**6 + 1)
# robot[i] := robot(i)의 부품의 개수
# 한부품은 1개의 로봇에만 속할수있다.!
# (2,3)  , (4,5 )
# (2,3,4,5) 가될때
# 어떻게  합쳐줄것인가?
for _ in range(n):
    temp = input()
    if temp[0] == 'I':
        #
        I,a,b = temp.split()
        # a,b 부모가 같은데 들어오면 반영 x
        x,y = find(parent,int(a)),find(parent,int(b))
        if x != y:
            if x < y :
                robot[x] += robot[y]
            else:
                robot[y] += robot[x]
        # a,b 부모가 다르면 한곳에 몰아주면됨
        # a와 b 의 부모를 연결
        union(parent,int(a),int(b))
    else:
        Q,c = temp.split()
        print(robot[find(parent,int(c))])