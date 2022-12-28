def solution(numlist, n):
    answer = []
    numlist.sort(key = lambda x: (abs( x - n),-x))
    return numlist