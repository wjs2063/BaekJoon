import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input())
    parent = defaultdict(int)
    for _ in range(n - 1):
        a,b = map(int,input().split())
        # b 의 부모는 a 이다
        parent[b] = a
    p,q = map(int,input().split())
    # 일단 p 와 q 의 레벨을 맞춰야하지않을까? 레벨도 사실모름... ?? HOW ?
    # 일단 한개를 먼저 다올려보내고
    # 조상이 같아지는 순간부터는 그뒤로 조상이 다 같을거아닌가
    # a b c d e f 라면
    # k m c d e f 겠지?
    # 그러면 공통은 c 일거고
    # x 에 p의 조상 싹다넣고
    x = set()
    # 루트의 조상이아닐때까지
    # p 가 q 의 조상이거나 q 가 p의 조상일수도있음
    while p != 0:
        x.add(p)
        p = parent[p]
    while q != 0:
        if q in x:
            break
        q = parent[q]
    print(q)