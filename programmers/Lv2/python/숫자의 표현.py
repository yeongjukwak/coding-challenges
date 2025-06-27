def solution(n):
    answer = 0
    number = 1
    q = [number]
    
    while number <= n:
        q_sum = sum(q)
        
        if q_sum > n:
            q.pop(0)
        else:
            if q_sum == n:
                answer += 1
            
            number += 1
            q.append(number)
    
    return answer
