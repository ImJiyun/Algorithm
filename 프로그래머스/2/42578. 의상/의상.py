from collections import defaultdict

def solution(clothes):
    d = defaultdict(list)
    for cloth, kind in clothes:
        d[kind].append(cloth)
    
    cnt = 1
    for kind in d:
        cnt *= len(d.get(kind))+1
        
    return cnt-1