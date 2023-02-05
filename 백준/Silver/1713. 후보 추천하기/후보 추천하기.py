import sys
input = sys.stdin.readline

n = int(input().strip())

vote_cnt = int(input().strip())

seq = list(map(int,input().split()))

# 사진틀의정보 := (추천횟수,들어온시각,학생번호)
pic = []
# 사진틀에 게시된 학생들의 목록 pic_st
pic_st = set()

for i,v in enumerate(seq):
    # 추천하려는 학생 번호 는 v
    # ㅇ ㅣ학생이 사진틀에 있는가 없는가?
    if v in pic_st:
        # 찾자
        # pic[j] -> (추천횟수,게시된 시각,학생번호)
        for j in range(len(pic)):
            if pic[j][2] == v:
                pic[j][0] += 1
                break
    # 꽉 차있으면
    elif len(pic) == n :
        # 정렬후 하나 지워
        pic.sort(key = lambda x:(-x[0],-x[1]))
        # 지우고
        x,y,z = pic.pop()
        # 학생번호 지우고
        pic_st.discard(z)
        pic.append([1,i,v])
        pic_st.add(v)
    else:
        pic.append([1,i,v])
        pic_st.add(v)
pic.sort(key = lambda x:(x[2]))
maxi = pic[0][0]
# 마지막에는
ans = []
for i in range(len(pic)):
    ans.append(pic[i][2])
print(*ans)