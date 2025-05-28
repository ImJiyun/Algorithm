def solution(array):
    counts = {}
    
    for num in array:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
    sorted_cnts = sorted(counts.items(), key=lambda item : item[1], reverse=True)
    
    rank_cnts = {}
    for k, v in sorted_cnts:
        if v not in rank_cnts:
            rank_cnts[v] = 0
        rank_cnts[v] += 1
            
    return sorted_cnts[0][0] if rank_cnts[sorted_cnts[0][1]] == 1 else -1