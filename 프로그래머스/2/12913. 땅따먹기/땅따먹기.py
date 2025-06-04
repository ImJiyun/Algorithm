def solution(land):
    prev = land[0]
    idx = 1
    
    while idx < len(land):
        cur = land[idx]
        new_row = [0] * 4

        for i in range(4):
            max_val = 0
            for j in range(4):
                if i == j:
                    continue
                max_val = max(max_val, cur[i] + prev[j])
            new_row[i] = max_val
            
        prev = new_row
        idx += 1
    
    return max(prev)