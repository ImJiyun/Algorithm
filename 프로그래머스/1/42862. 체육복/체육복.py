def solution(n, lost, reserve):
    overlap = set(lost) & set(reserve)
    
    lost = sorted(set(lost)-overlap)
    reserve = sorted(set(reserve)-overlap)
    
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    return n - len(lost)