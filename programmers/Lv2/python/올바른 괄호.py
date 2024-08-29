def solution(s):  
    res = []
    
    for val in list(s):
        if val == ')' and len(res) > 0:
            res.pop()
        elif val == '(':
            res.append(val)
        else:
            return False
    
    return True if len(res) == 0 else False
