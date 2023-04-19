import sys
input = sys.stdin.readline

n = int(input())

students = []

for _ in range(n):
    students.append(list(map(int,input().split())))
ans = []
for i,v in enumerate(students):
    friends = set()
    for j in range(5):
        cls = v[j]
        for k in range(n):
            if k == i :continue
            if students[k][j] == cls:
                friends.add(k)
    ans.append([i + 1,len(friends)])
ans.sort(key = lambda x:(-x[1],x[0]))

print(ans[0][0])