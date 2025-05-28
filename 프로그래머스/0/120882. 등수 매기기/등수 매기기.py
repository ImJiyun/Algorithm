def solution(score):
    
    avgs = [sum(s)/2 for s in score]
    
    sorted_avgs = sorted(avgs, reverse=True)
    
    rank_map = {}
    for i, s in enumerate(sorted_avgs):
        if s not in rank_map:
            rank_map[s] = i + 1
            
    answer = [rank_map[a] for a in avgs]
    return answer