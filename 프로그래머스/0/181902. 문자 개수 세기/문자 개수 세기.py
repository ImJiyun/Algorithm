def solution(my_string):
    answer = [0 for _ in range(52)]
    
    for ch in my_string:
        if 'A' <= ch <= 'Z':
            answer[ord(ch) - ord('A')] += 1
        elif 'a' <= ch <= 'z':
            answer[ord(ch) - ord('a') + 26] += 1
        
    return answer