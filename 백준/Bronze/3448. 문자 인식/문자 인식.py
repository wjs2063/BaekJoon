import sys
from collections import Counter
input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    answer = ""
    while True:
        x = input().strip()
        if x == "":
            break
        answer += x
    a = len(answer)
    t = Counter(answer)
    rr = round(100 * (a - t["#"]) / a,1)
    if int(rr) == rr:
        rr = int(rr)
    print(f"Efficiency ratio is {rr}%.")