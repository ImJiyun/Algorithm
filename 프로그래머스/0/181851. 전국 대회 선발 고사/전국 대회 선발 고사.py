def solution(rank, attendance):
    filtered = [(i, rank[i]) for i in range(len(rank)) if attendance[i]]
    
    filtered.sort(key=lambda x: x[1])
    
    a, b, c = filtered[0][0], filtered[1][0], filtered[2][0]
    
    return 10000 * a + 100 * b + c