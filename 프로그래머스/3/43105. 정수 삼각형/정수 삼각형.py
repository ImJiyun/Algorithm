def solution(triangle):
    row_cnt = len(triangle)
    prev = triangle[0]
    cur_idx = 1
    
    while cur_idx < row_cnt:
        cur = triangle[cur_idx]
        temp = [0] * len(cur)
        
        for i in range(len(cur)):
            num = 0
            if i == 0:
                temp[i] = cur[i] + prev[0]
            elif i == len(cur)-1:
                temp[i] = cur[i] + prev[-1]
            else:    
                temp[i] = cur[i] + max(prev[i-1], prev[i])
        
        prev = temp
        cur_idx += 1
    
    max_val = max(prev)
    return max_val