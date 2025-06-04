from collections import defaultdict

def solution(weights):
    N = len(weights)
    
    cnt = 0
    
    d = defaultdict(int)
    
    for w in weights:
        cnt += d[w] + d[w * 2] + d[w * 0.5] + d[w * 2/3] + d[w * 3/2] + d[w * 3/4] + d[w * 4/3]
        d[w] += 1
        
    return cnt