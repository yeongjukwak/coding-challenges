def solution(price):
    if price >= 500000:
        result = int(price * 0.8)
    elif price >= 300000:
        result = int(price * 0.9)
    elif price >= 100000:
        result = int(price * 0.95)
    else:
        result = price
    
    return result
