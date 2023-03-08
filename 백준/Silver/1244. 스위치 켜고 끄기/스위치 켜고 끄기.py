import sys
input = sys.stdin.readline

n = int(input().strip())

sw = list(map(int,input().split()))

t = int(input())
# 남학생이면
def excute(sex,sw_num):
    if sex == 1:
        for i in range(1,n + 1):
            if i % sw_num == 0:
                sw[i - 1] ^= 1
    else:
        for interval in range(min(n - sw_num,sw_num - 1),-1,-1):
            l,r = sw_num - interval,sw_num + interval
            if sw[l - 1:r] == sw[l - 1:r][::-1]:
                for k in range(l - 1,r):
                    sw[k] ^= 1
                break

for _ in range(t):
    a,b = map(int,input().split())
    excute(a,b)

for i in range(0,len(sw),20):
    l,r = i,i + 20
    print(*sw[l:r])