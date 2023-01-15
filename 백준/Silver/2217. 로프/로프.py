import sys
input = sys.stdin.readline

n = int(input())

info = []

for _ in range(n):
    info.append(int(input()))

# 예를들면 3 3 3 10 10  이라면 -> 답은 20 이됨.
# 로프를 몇개사용할 것인가???
# 역순으로 정렬
# a,b,c,d,e 가있으면 5개 다 사용하게되면 min(a,b,c,d,e)*5 가 답임
answer = 0
#O(NlogN)
info.sort(reverse = True)
# info[i]*(i + 1) := 내림차순이니까 0 ~ i번째 까지 로프를 사용할것( info[i]가 최소 ) * ( 로프개수)

#O(N)
for i in range(len(info)):
    answer = max(answer,info[i]*(i + 1))
print(answer)

# O(nlogn) 으로 해결가능

"""
5
3
3
3
10
10
답 : 20


"""