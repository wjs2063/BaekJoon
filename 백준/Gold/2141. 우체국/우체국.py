import sys

si = sys.stdin.readline

n = int(si().strip())

pos = []

"""
Solution

https://blog.naver.com/jahy5352/223385505572

점3개가 있다고 가정하자, t1,t2,t3 는 위치이며 p1,p2,p3 는 각 위치에 대한 사람수이다.
그러면 다음과같은 수식이 성립한다. 시그마(1부터 3까지) pk * |x - tk | (x 는 우체국 위치)
다음 식이 최소가 되게하는 x값을 구하는게목표이다.

그러면 차근차근 규칙을 찾아보자 

t1,t2,t3 가 각각 1,2,3 이라 가정하자 
p1 * | x - 1 | + p2 * | x - 2 | + p3 * | x - 3 | 이 된다. 구간을 나누자 (4개의구간이나오게된다)

무엇이던 일차함수 or 상수함수가 나오리라고는 충분히 예측할수있다.

제일 왼쪽은 (-p1 -p2 -p3 ) * x + 어떤 상수값 정도로 나온다 이말 즉 기울기가 음수인 일차함수다 아래로떨어지겠지
다음은 +p1 - p2 - p3 정도다 , 과연 이 기울기는 양수일까 음수일까? 모른다. 
하지만 음수라면 ? 더 감소하는형태가 될것이다.상상해보자 그림을! 
양수라면 ?? 더이상 올라가는형태만 남게된다. 이다음 스텝은 +p1 - p2 - p3 일텐데 모든 pk는 양수기때문이다! 

자 그러면 언제 - 에서 + 로 변하는가? 를 알면 답이나온다. 첫 + 인경우 제일 그구간의 좌측값 답이되겠지 


먼저 tk 에 대해서 정렬해야한다.
"""

for _ in range(n):
    # 위치 사람수
    x, p = map(int, si().split())
    pos.append([x, p])
# 위치로 정렬한다
pos.sort(key=lambda x: (x[0],-x[1]))

right = 0
# 누적합을 사용해보자
for x, p in pos:
    right -= p
left = 0
# 초기값은 항상 제일 왼쪽으로 둔다
ans = pos[0][0]
for idx in range(n - 1):
    x, p = pos[idx]
    right += p
    left += p

    if left + right >= 0 :
        break
    # 음수인경우니까 오른쪽 갱신
    ans = pos[idx + 1][0]
print(ans)