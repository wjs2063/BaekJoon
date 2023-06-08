import sys 
input = sys.stdin.readline 
t = int(input())

words = []

for _ in range(t):
    words.append(input().strip())

for word in words:
    if word[::-1] in words:
        print(len(word),word[len(word) // 2])
        break 