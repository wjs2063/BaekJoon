s=input()
s=s.upper()

ele=set(s)
answer=[]
for e in ele:
    count=0
    for i in range(len(s)):
        if s[i]==e:
            count+=1
    answer.append([count,e])

answer.sort(reverse=True)
if len(answer)==1:
    print(answer[0][1])
elif answer[0][0]==answer[1][0]:
    print("?")
else :
    print(answer[0][1])
    

