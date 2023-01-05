import sys
input = sys.stdin.readline

n,m = map(int,input().split())
# 기차가 n 개 , m개의 명령
train = [0]*(n + 1)
# train[x] := x번째 기차 의 상태
# 2진수 000111
for _ in range(m):
    # 타입 ,기차번호, 좌석
    x = input()
    # 승차
    if x[0] == '1':
        a,b,c = map(int,x.split())
        train[b] |= ( 1 << c)
    # 하차 -> 1 이면 0으로 만들고 0이면 0으로
    #3번째 승객 하차 ex 1100 ->  1000
    #      ~0100  -> 1011
    #                1000
    elif x[0] == '2':
        a,b,c = map(int,x.split())
        train[b] &= ~(1 << c)
    # 뒤로가기
    elif x[0] == '3':
        c,b = map(int,x.split())
        # 20번째에 사람이 앉아있으면 제거해주고
        train[b] <<= 1
        train[b] &= ~ ( 1 << 21)
    else:
        # 1칸씩 뒤로
        c,b = map(int,x.split())
        # 0번쨰칸 제거 ,
        train[b] >>= 1
        train[b] &= ~1
# state 를 기록해서 카운트
visit = set()
cnt = 0
for i in range(1,n + 1):
    if train[i] in visit:
        continue
    cnt += 1
    visit.add(train[i])
print(cnt)