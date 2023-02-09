def solution(book_time):
    answer = 0
    arr = [0]*(60*24 + 11)
    for time in book_time:
        sn,en = time
        sh,sm = map(int,sn.split(":"))
        eh,em = map(int,en.split(":"))
        # 시작에는 1 
        arr[60*sh + sm] += 1
        # 청소시간까지 포함
        # 종료시점 에는 - 1
        arr[60*eh + em + 10 ] += -1
    for i in range(1,len(arr)):
        arr[i] += arr[i - 1]
    return max(arr)