import sys
input = sys.stdin.readline

t = int(input().strip())



for _ in range(t):
    n = int(input())
    arr = []
    junior = 1
    for _ in range(n):
        a,b = map(int,input().split())
        arr.append((a,b))
    arr.sort(key = lambda x:(x[0]))
    f = arr[0][1]
    # 서류성적을 오름차순 정렬을 해놓자
    # 이제는 이때까지 지나온 지원자들의 면접성적중 가장 높은 면접성적을 기록해
    for i in range(1,n):
        # 이떄까지 나왔던 면접성적보다 더 높거나 같으면 가능하다
        # f 에 해당하는 지원자가 가능하다는 소리다.
        if arr[i][1] < f :
            f = arr[i][1]
            junior += 1
    print(junior)