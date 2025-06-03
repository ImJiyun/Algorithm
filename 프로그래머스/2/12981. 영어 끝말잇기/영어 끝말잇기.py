def solution(n, words):
    
    visited = []
    
    for i, word in enumerate(words):
        if word in visited or (i > 0 and words[i-1][-1] != words[i][0]) or len(word) <= 1:
            return [i % n + 1, i // n + 1]
        visited.append(word)

    return [0, 0]