import sys
input = sys.stdin.readline

mbti = input().strip()

info = "INFP"

opp = dict()

for i,v in enumerate("ESTJ"):
    opp[v] = info[i]
    opp[info[i]] = v


ans = ""

for x in mbti:
    ans += opp[x]
print(ans)