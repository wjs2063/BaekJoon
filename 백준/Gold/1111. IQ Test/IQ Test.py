n=int(input())
solution=list(map(int,input().split()))
a=set()
'''
case 1: 길이가 2개일때 x1=x2 라면 답은 x1 임 (a=0인것에 해당)
case 2: 길이가 2개이고 x1!=x2 라면 답은 여러개가 될수있음 (변수 1개 free value)
case 3: 길이가 3개이상일때 연립일차방정식의 해의 가능성을 check 해보면됨
x1=x2 이고 x2=x3 라면 답은 무수히많음 
case 4: x1=x2 이고 x2!=x3 라면 답은 없음 
case 5: x1!=x2 라면 기울기가 달라 해가 존재함,set 으로 해가 유일한지 판단하기
'''
# 1개면 A
if n==1:
    print("A")
elif n==2:
    if solution[0]==solution[1]:
        print(solution[0])
    else:
        print("A")
# n은 3이상일떄
# 2 2 4 와 2 2 2 인경우를 보자 
# 2 2 4 는 불가능 2 2 2 는 2a+b=2 만족하는 a,b 모두 a=0으로 두자
else:
    if solution[0]==solution[1]:
        m=0
        p=solution[1]
    else :
        m=(solution[1]-solution[2])//(solution[0]-solution[1])
        p=solution[1]-m*solution[0]
    is_same_pattern=True
    for i in range(1,n):
        if solution[i]==solution[i-1]*m+p:
            continue
        else:
            is_same_pattern=False
            break
    if is_same_pattern:
        print(solution[n-1]*m+p)
    else:
        print("B")