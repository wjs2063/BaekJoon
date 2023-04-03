import sys
input = sys.stdin.readline


n = int(input())
cc = list(map(int,input().split()))
m = int(input())

box = list(map(int,input().split()))
cc.sort(reverse = True)
box.sort()

if max(box) > max(cc):
    print(-1)
else:
    time = 0
    # box 가있을떄까지 돌면서
    while box:
        for c in cc :
            # 크레인을 돌면서 가장 많이담을수있는 크레인에 무거운 박스를 넣자
            if not box:break
            # 현재 크레인 c 에 담을수있는 제일 무거운 박스를 찾자
            j = len(box) - 1
            while box and j >= 0:
                if box[j] <= c:
                    box.pop(j)
                    break
                j -= 1
        time += 1
    print(time)
    
