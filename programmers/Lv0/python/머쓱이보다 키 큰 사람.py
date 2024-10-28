def solution(array, height):
    answer = []
    
    for arr in array:
        if arr > height:
            answer.append(arr)
    
    return len(answer)
