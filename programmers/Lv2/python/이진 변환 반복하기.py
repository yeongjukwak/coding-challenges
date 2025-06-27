def solution(s):
    convert_cnt = 0
    zero_cnt = 0
    
    while s != '1':
        s_len = len(s)
        s_len_rmzero = len(s.replace('0', ''))
        
        convert_cnt += 1
        zero_cnt += (s_len - s_len_rmzero)
        
        s = bin(s_len_rmzero).replace('0b', '')
    
    return [convert_cnt, zero_cnt]
