import sys
input = sys.stdin.readline

n = int(input().strip())
word = []
for _ in range(n):
    word.append(input().strip())
word = list(set(word))
word.sort(key = lambda x:(len(x),x))
for x in word:
    print(x)