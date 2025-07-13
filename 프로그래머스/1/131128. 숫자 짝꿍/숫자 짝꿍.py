from collections import defaultdict

def solution(X, Y):
    count_X = defaultdict(int)
    count_Y = defaultdict(int)
    
    for ch in X:
        count_X[ch] += 1
    for ch in Y:
        count_Y[ch] += 1
        
    result = []
    for digit in reversed(range(10)):
        d = str(digit)
        common = min(count_X[d], count_Y[d])
        result.extend([d] * common)
        
    if not result:
        return '-1'
    
    if result[0] == '0':
        return '0'
    
    return ''.join(result)