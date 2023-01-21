import sys
input = sys.stdin.readline
one = list(map(int,input().split()))
two = list(map(int,input().split()))
# one 에 사과를 담을건지 오렌지를 담을건지 선택 뭐가이득인지 선택
print(min(two[0] + one[1],two[1] + one[0]))
