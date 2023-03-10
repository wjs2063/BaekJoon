import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

n = int(input().strip())

arr = []
for _ in range(n):
    arr.append(int(input().strip()))
t = defaultdict(int)

# 기본적으로 1개는 필요함

# 언제 늘려야하냐?
# 1 3 5 6 7 이미 오름차순이면  늘릴필요 x
# 1 5 3 6 7 ->  1담고  5 3 이 반전이니까 -> 5 따로담고 -> 1 3 -> 5 6 7 -> 2개필요하네

#  그러면 a1 < a2 > a3 < a4 < a5 > a6 이라고할때
#  1 5 3 4 7 6 -> 1 -> 5 따로 -> 1 3 4 , 5  , 6 7  -> 3 개
#  1 3 4 5 6 7

#  3 5 1 4 7 6 -> 정렬했을떄 자기가 있어야 할위치?

# 1 3 4 5 6 7

# 데크를 이어붙혀서 오름차순만드려면 일단은 데크자체도 오름차순정렬이 되어있어야함 그대신 겹치는구간이없어야겠지

# 1 ->

cc = sorted(arr[:]) # 정렬본
for i,x in enumerate(cc):
    t[x] = i
# 각 숫자마다 정렬본한테 물어보는거지. 너 양옆에 들어갈수있는지

temp = [ deque([arr[0]]) ]
# 1개는 무조건 필요함
# n 은 50이니까 시간은 넉넉함
for i in range(1,n):
    num = arr[i]
    # num 이라는 숫자가 temp( 계속 순회하면서 물어봐) 내가들어갈곳있어?
    # 언제 들어갈수있냐? 정렬되었을때 num 바로 옆에있는 애들이면 가능하지
    # 바로옆에있는 애들이없으면 새로만들어야함
    # O(N)
    x = t[num]
    flag = True
    # 각자 deque 는 오름차순 정렬로 유지시켜놓는다 !! 어떤 시점에서도 데크내에서는 오름차순이 유지됨
    # 현재 생성된 deque 를 다 돌면서 물어보는구간
    for j in range(len(temp)):
        # 인덱스 범위체크하고
        if x - 1 >= 0 :
            # 오른쪽에 들어갈곳인지 cc[x - 1] < num < cc[x + 1] 을 항상 만족하므로
            if temp[j][-1] == cc[x - 1]:
                temp[j].append(num)
                flag = False
                break
        if x + 1 < n  :
            if temp[j][0] == cc[x + 1]:
                temp[j].appendleft(num)
                flag = False
                break
    # 만약 넣을곳이없으면?
    if flag:
        temp.append(deque([num]))
print(len(temp))


# ex

# sub

#1 5 3 4 7 6 -->   ( 1,3,4)  , ( 5 )  , (7  )

#1 3 4 5 6 7 -->




