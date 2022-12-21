import sys
n,c=map(int,sys.stdin.readline().split())
home=[]
for _ in range(n):
    home.append(int(sys.stdin.readline()))
home.sort()
start=1
end=home[-1]-home[0]
#start 는 최소거리 1 end 는 최대거리 
answer=0

while start<=end:
    mid=(start+end)//2
    ol=home[0]
    cnt=1
    for i in range(1,len(home)):
        #거리가 mid 이상이면 공유기 설치
        if home[i]-ol>=mid:
            cnt+=1
            ol=home[i]
    if cnt>=c:
        start=mid+1
        answer=mid
    else:
        end=mid-1
print(answer)