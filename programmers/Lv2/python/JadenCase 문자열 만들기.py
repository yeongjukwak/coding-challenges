def solution(s):
    answer = ''
    
    prev_c = ' '
    for c in s:
        answer += c.upper() if prev_c == ' ' else c.lower()
        prev_c = c
    
    return answer
