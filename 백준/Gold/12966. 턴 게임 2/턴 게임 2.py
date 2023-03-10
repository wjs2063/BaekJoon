import sys
input = sys.stdin.readline

x,y = map(int,input().split())

# 1 2 3 4 5 6
# 1 3 5 7 9 11

# 윤호가 a번 승 b 번패하면  동혁이는 b 번승 a 번 패하게된다

# 즉 a + b 가 총 라운드 횟수가 됨을 의미함
# n번 라운드를 진행하게되면 총 점수는 n^2 이 된다. ( 홀수의 합)

# 모든점수합이 n^2 이 되면 일단은 가능하게됨

#  n 라운드중 윤호가 x 점을 획득하려면 x 점을 2n - 1 이하의 작은 홀수의 합으로 표현해야겟지?

# x 점을 2n - 1 이하의 홀수들로 구성해야함 ( 단 최소개수로 )

# 최소 x 번이므로 윤호는 최대한 많은점수를 획득하는 방향으로 가야함

# 20 16 점을 예로들면 총 6라운드 진행
# 답은 2번 -> 1 3 5 7 9 11 -> (11,9)


# 34 2  -> 불가능 ? 어떻게판별? 완탐으로 가능은 할거같은데 시초나겠고
# 33 3  -> 가능
# 128 128 -> 2^8 이므로 16라운드 까지진행하게된다. 1 ~ 31 점까지 조합으로 나타내자.
# 129 127 ->
# 29 7  -> 가능

# 다시 풀어보면 1,3,5,7,9,. . . 2i - 1 일때 -> 합은 i^2 이 되고
# 1 <= 정수 <= i^2 인데 이 정수를 1 ~ 2i - 1 의 합으로 나타낼수있냐없냐?
# 2는 일단 안돼
# 생각해보자 i^2 에서 -> i^2 - 1 , 1 가능
# i^2 - 2, 2 불가능
# i^2 - 3 , 3 -> 3 하나쓰고 나머지몰빵
# i^2 - 4 , 4 -> 1,3 하나쓰고 몰빵
# i^2 - 5 , 5 -> 2,3 몰빵
# i^2 - (2i - 1) ->
# i^2 - (2i - 3) ->
n = x + y
# 완전제곱 꼴이아니면 불가능 x + y = n^2 꼴이므로
if n**0.5 != int(n**0.5):
    print(-1)
else:
    # 2는 표현이 불가능하다
    if x == 2 or y == 2:
        print(-1)
    # 0이면 그냥 0
    elif x == 0 :
        print(0)
    # round
    else:
        rd = int(n**0.5)
    # 그냥 높은점수부터 뺴주자
    # 1 3 5 7 9    5라운드
    # 18 7 -> 9 에서 7추가할때 2 점은 못채운다 -> 이 2점간격을 다음칸 5 3 1 로?
        answer = 0
        for i in range(rd,1,-1):
            if x >= 2*i - 1:
                x -= 2*i - 1
                answer += 1
            # 2점이거나 1점이면
            if x <= 2:
                break
        answer += x
        print(answer)





