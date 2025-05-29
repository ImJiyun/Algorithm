def solution(numlist, n):
    
    dist = [(num, abs(n - num)) for num in numlist]
    
    dist.sort(key=lambda x: (x[1],  -x[0]))
    
    return [num for num, _ in dist]