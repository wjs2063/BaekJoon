import sys
from itertools import permutations
input = sys.stdin.readline

k = int(input())

relation = input().split()

nums = [str(i) for i in range(10)]
# k + 1 개 택하고
ccc = permutations(nums,k + 1)
ans = []
for cc in ccc:
    l = 0
    temp = ""
    for i in range(k):
        if relation[i] == "<":
            if cc[l] < cc[l + 1]:
                temp += cc[l]
            else:
                break
        else:
            if cc[l] > cc[l + 1]:
                temp += cc[l]
            else:
                break
        l += 1
        # 마지막이면
        if i == k - 1:
            temp += cc[l]
            ans.append(temp)
ans.sort()
print(ans[-1])
print(ans[0])
