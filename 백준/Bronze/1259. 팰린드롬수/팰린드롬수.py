import sys
input = sys.stdin.readline

while True:
    x = input().strip()
    if x == "0":break
    if x == x[::-1]:
        print("yes")
    else:
        print("no")