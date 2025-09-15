from collections import defaultdict

def solution(participant, completion):
    d = defaultdict(int)
    
    for p in participant:
        d[p] += 1
    for p in completion:
        d[p] -= 1
        if d[p] == 0:
            del d[p]
    return list(d.keys())[0] 