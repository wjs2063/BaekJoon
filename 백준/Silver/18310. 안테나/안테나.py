import sys
input = sys.stdin.readline


# 풀이전략

"""
결국 구하고자하는것
for k in range(1,n + 1):
    temp = 0
    for i in range(1, n + 1):
         k번쨰집과 i번쨰집의 거리의 최솟값을 찾는것이다 
        temp += abs(arr[i] - arr[k]) 
수식으로는 시그마와 min 을 사용하면 간단함

어쨋던 이 식을 펼쳐보면 |x - a | + |x - b | + |x - c| .. . .등으ㅢ 최솟값이다. 이 x값을 구하는것
이를 잘 관찰해보면 최솟값일때는  홀수일때와 짝수일때로 나뉜다 
# 홀수일때는 n = 5개중 index 3 - 1번쨰가 답이고
# 짝수일때는 n = 6 index가 3 - 1과 4 - 1일떄가 답이다(문제에서는 3이답일것)
"""

n = int(input().strip())
arr = list(map(int,input().split()))
arr.sort()
print(arr[n // 2 - 1] if n % 2 == 0 else arr[n // 2] )
