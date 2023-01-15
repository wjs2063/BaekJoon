import sys
input = sys.stdin.readline
from _collections import defaultdict
import heapq
n = int(input().strip())

h = []

for _ in range(n):
    a,start,end = map(int,input().split())
    heapq.heappush(h,(start,end,a))
# room := 사용가능한 강의실번호 (최악으로 n개모두사용해야할수도있다)
room = [i for i in range(1, n + 1)]
# heap 으로 만들어주고 사용가능한 강의실중 최소강의실번호를 배정해줄것
heapq.heapify(room)
# cc에는 강의를 어떤 강의실에 배정할거냐! cc[3] -> 3번강의는 cc[3]의값에 배정되어있음
cc = defaultdict(int)
# temp 라는 애는 추가강의실이 필요한 애들을 넣어놓는곳
temp = []
answer = 0
while h:
    #현재강의의 시작, 종료, 강의 넘버
    start,end,course_num = heapq.heappop(h)
    #temp 에 들어있는 애들중 가장빨리끝나는 강의의 종료시점이 시작지점보다 이전이라면
    while temp and temp[0][0] <= start:
        #한개씩 뺴서
        en,rr = heapq.heappop(temp)
        # 사용가능한 room 에 추가해줍니다
        heapq.heappush(room,rr)
    # 이제는 사용가능한 room 이 확실해졌으니
    r = heapq.heappop(room)
    # 강의실배정하자
    heapq.heappush(temp,(end,r))
    cc[course_num] = r
    answer = max(answer,len(temp))
print(answer)
for i in range(1,n + 1):
    print(cc[i])