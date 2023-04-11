import sys
import re
input = sys.stdin.readline


n = int(input())

pattern = input().strip().replace("*",".*")
p = re.compile(pattern)
for _ in range(n):
    s = input().strip()
    res = p.fullmatch(s)
    if res:print("DA")
    else:print("NE")
