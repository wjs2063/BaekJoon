import sys
si = sys.stdin.readline

t = int(si())



for _ in range(t):
    xx = map(int,si().split())
    odd,even = 0,0
    for x in xx:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    if even >= 2:
        print("R")
    else:
        print("B")


    #전체 돌의 상태
    #짝 짝 짝 R
    #짝 짝 홀 R
    #짝 홀 홀 B
    #홀 홀 홀 B

# 상태

# (x,y,z) -> (x + 1,y - 1 ,z - 1) or (x - 1,y + 1,z - 1) ,(x - 1,y - 1,z + 1) 3가지상태로 넘어갈수있다
# 돌은 매 라운드마다 1개씩줄어든다.