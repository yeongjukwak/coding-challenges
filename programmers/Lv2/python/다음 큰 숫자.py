def solution(n):
    answer = 0
    n_cnt = bin(n)[2:].count('1')
    
    while True:
        n += 1
        
        if n_cnt == bin(n)[2:].count('1'):
            answer = n
            break
    
    return answer
