import math


def solution(progresses, speeds):
    answer = []
    update_cnt = 0
    update_date = 0
    
    for idx, val in enumerate(progresses):
        tmp = math.ceil((100 - val) / speeds[idx])
        
        if idx == 0:
            update_date = tmp
            update_cnt = 1
        elif update_date >= tmp:
            update_cnt += 1
        else:
            update_date = tmp
            answer.append(update_cnt)
            update_cnt = 1
    
    answer.append(update_cnt)
    
    return answer
