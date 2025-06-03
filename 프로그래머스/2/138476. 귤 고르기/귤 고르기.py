from collections import defaultdict

def solution(k, tangerine):
    d = defaultdict(int)
    
    for fruit in tangerine:
        d[fruit] += 1
        
    arr = sorted(list(d.items()), key=lambda x: x[1], reverse=True)
    
    for idx, (size, cnt) in enumerate(arr):
        if k <= 0:
            return idx
        k -= cnt
        
    return len(arr)