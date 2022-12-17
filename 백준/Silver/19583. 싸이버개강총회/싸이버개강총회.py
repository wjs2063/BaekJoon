import sys
from collections import defaultdict
input = sys.stdin.readline
enter = defaultdict(int)
out = defaultdict(int)
people = set()
start ,end,streaming_end = input().split()
while 1:
    try :
        temp = input()
        chat_time,user = temp.split()
        people.add(user)
        if chat_time <= start :
            enter[user] = 1
        if end <= chat_time <= streaming_end :
            out[user] = 1
    except :
        break
answer = 0
for p in people :
    if enter[p] & out[p] :
        answer += 1
print(answer)
