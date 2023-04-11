import sys
import re
input = sys.stdin.readline


n = int(input())

pattern = input().strip().replace("*",".*")

for _ in range(n):
    s = input().strip()
    res = re.fullmatch(pattern,s)
    if res:print("DA")
    else:print("NE")
