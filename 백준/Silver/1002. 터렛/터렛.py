import sys
input=sys.stdin.readline
n=int(input())

for _ in range(n):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    distance=(x1-x2)**2+(y1-y2)**2
    radius_out_square=(r1+r2)**2
    radius_in_suqare=(r1-r2)**2
    if r2>r1:
        x1,y1,r1,x2,y2,r2=x2,y2,r2,x1,y1,r1
    #원 내부,외부 
    if (x1,y1)==(x2,y2) and r1==r2:
        print(-1)
    elif distance<r1**2:
        if distance<radius_in_suqare:
            print(0)
        elif distance==radius_in_suqare:
            print(1)
        else:
            print(2)
    elif distance==r1**2:
        if r2<2*r1:
            print(2)
        elif r2==2*r1:
            print(1)
        else:
            print(0)
    else:
        if distance<radius_out_square:
            print(2)
        elif distance==radius_out_square:
            print(1)
        else:
            print(0)
            