from collections import defaultdict

def solution(participant, completion):
    d = defaultdict(int)
    
    for person in participant:
        d[person] += 1
    
    for person in completion:
        d[person] -= 1
        if d[person] == 0:
            del d[person]
            
    return next(iter(d))