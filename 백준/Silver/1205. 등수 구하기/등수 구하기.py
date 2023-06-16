import sys
input = sys.stdin.readline

n,new_score,p = map(int,input().split())

if n  :
    rank = list(map(int,input().split()))
    rank.sort(reverse = True )
else:
    rank = []

# 0 <= n <= p
# 10 <= p <= 50

# 새로운 스코어가 바로 들어갈수있는 상황이라면 ?
if len(rank) < p :
    rank.append(new_score)
    rank.sort(reverse = True)
    print(rank.index(new_score) + 1)
# 꽉찼지만 이전점수들중 하나보다 더좋은경우
elif new_score > rank[-1]:
    rank.pop()
    rank.append(new_score)
    rank.sort(reverse = True)
    print(rank.index(new_score) + 1)
# 새로운점수가 이전점수보다 좋지않은경우는 -1
else:
    print(-1)
