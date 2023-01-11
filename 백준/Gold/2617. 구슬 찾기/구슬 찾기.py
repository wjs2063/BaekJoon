import sys
sys.setrecursionlimit(10**6)
from _collections import defaultdict
input = sys.stdin.readline

n,m = map(int,input().split())
smallest = defaultdict(set)
biggest = defaultdict(set)
for _ in range(m):
    # a > b
    # smallest[a] := [ b1,b2,b3] -> a보다 작은것들이 b1,b2,b3 가있다는 의미
    # biggest[b] := [a1,a2,a3] -> b 보다 큰것들이 a1,a2,a3 가있다는 의미
    a,b = map(int,input().strip().split())
    smallest[a].add(b)
    biggest[b].add(a)
# dfs 순회하면서 계속 상대적인 계산을 계속 진행해본다
#큰것들의 개수담기 즉 big[x] : int 의 의미 -> x 보다 큰것들의개수
big = defaultdict(set)
#작은것들의 개수 담기 small[x] :int 의 의미 -> x 보다 작은것들의 개수
small = defaultdict(set)
# 예를들어서 4 > 2 , 2 > 1 이 주어져있으면 4 > (2, 1) 인것을 확인해내자는말이다
# bead -> 현재 구슬 번호



# 자 이제 중간구슬의 특징을 보자
# N 이 홀수이기때문에 항상 중간구슬이 존재한다 (중앙값 찾는문제가아님)
# 예를들어 n 이 5이면 중간구슬은 3 이다 , 즉 나보다 작은애들이 2개, 큰애들이 2개씩존재한다
# mid = n // 2 이고 작거나 큰것들의 개수가 mid 보다 크면 불가능하겠지
# 각 구슬별로 작거나 큰것들의 개수를 구하는게 핵심이되겠다.
# 1 > [3,5] 인데 3 보다작은게 2개 5보다 작은게 2개 라면 1보다작은것은 6개다

# dfs1(bead) 의 의미 bead 보다 무게가 작은것들의 개수를 return 해준다,
def dfs1(bead):
    global smallest
    global small
    # 이미 계산된 경우면 그대로 return
    # 카운팅하기
    for next_bead in smallest[bead]:
        small[bead].add(next_bead)
        small[bead] |= dfs1(bead)
    return small[bead]
# dfs2(bead) 의 의미 bead 보다 무게가 큰것들의 개수를 return
def dfs2(bead):
    global biggest
    global big
    #계산됐으면 종료
    # answer 의 초기값 : 현재 구슬(bead) 보다 작은것들의 개수 , 작은구슬을 돌면서 dfs
    for next_bead in biggest[bead]:
        big[bead].add(next_bead)
        big[bead] |= dfs2(next_bead)
    return big[bead]
# 각 구슬마다 dfs 돌려주자

############################### 위 dfs 는 메모리초과뜸.#############
from _collections import deque
def bfs1(start):
    q = deque([start])
    visited = [0]*(n + 1)
    visited[start] = 1
    cnt = 0
    while q:
        x = q.popleft()
        cnt += 1
        for next_node in biggest[x]:
            if visited[next_node]:continue
            visited[next_node] = 1
            q.append(next_node)
    return cnt - 1 # 자기자신은 제외해주자
def bfs2(start):
    q = deque([start])
    visited = [0]*(n + 1)
    visited[start] = 1
    cnt = 0
    while q:
        x = q.popleft()
        cnt += 1
        for next_node in smallest[x]:
            if visited[next_node]:continue
            visited[next_node] = 1
            q.append(next_node)
    return cnt - 1 # 자기자신은 제외해주자

mid = n // 2
answer = 0
for i in range(1, n  + 1):
    if bfs1(i) > mid or bfs2(i) > mid :
        answer += 1
print(answer)

'''
test case 

3 2
2 1
3 1
답 : 1

5 5
1 3
1 5 
4 3
4 5
2 5
답 : 1


5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
답 : 4
'''