def solution(elements):
    answer = 0
    N = len(elements)
    elements = elements + elements
    sums = set()
    
    for i in range(1, N+1):
        for j in range(N):
            sums.add(sum(elements[j:j+i]))
        
    return len(sums)