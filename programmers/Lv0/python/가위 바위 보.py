def solution(rsp):
    answer = ''
    
    for data in rsp:
        if data == '2':
            answer += '0'
        elif data == '0':
            answer += '5'
        else:  # data == '5'
            answer += '2'
    
    return answer
