import re
from collections import deque
my_str=input().rstrip()
explosion_str=input().rstrip()

def solution2(my_str,explosion_str):
    last=explosion_str[-1]
    stack=list()
    l=len(explosion_str)
    for strs in my_str:
        # 문자추가
        stack.append(strs)
        if strs==last and "".join(stack[-l:])==explosion_str:
            #삭제
            del stack[-l:]
    answer="".join(stack)
    if answer=="":
        print("FRULA")
    else :
        print(answer)
solution2(my_str,explosion_str)