from collections import defaultdict
def solution(today, terms, privacies):
    answer = []
    # terms 
    # A month 형태 
    # privacies 
    # Year.month.days type
    p_date = defaultdict(int)
    y,m,d = map(int,today.split('.'))
    today = 12*28*y + 28*m + d
    for term in terms:
        x,y = term.split()
        p_date[x] = y

    for i,privacy in enumerate(privacies):
        date,tp = privacy.split()
        d = p_date[tp]
        year,month,day = map(int,date.split('.'))
        month += int(d)
        while month > 12:
            year +=1 
            month -= 12
        date = str(year) + str(month) + str(day)
        s = year*12*28 + month*28 + day - 1
        if s < today:
            answer.append(i + 1)
        
        
    return answer