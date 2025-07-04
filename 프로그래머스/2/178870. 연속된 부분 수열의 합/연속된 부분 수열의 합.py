def solution(sequence, k):
    N = len(sequence)
    answer = [0, N-1] 
    left, right, total = 0, 0, 0
    
    while right < N:
        total += sequence[right]
        while total > k:
            total -= sequence[left]
            left += 1
        if total == k:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
        right += 1
    return answer