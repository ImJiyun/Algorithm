def solution(name, yearning, photo):
    answer = []
    dic = dict()
    for k, v in zip(name, yearning):
        dic[k] = v
    
    for r in range(len(photo)):
        total = 0
        for c in range(len(photo[r])):
            if photo[r][c] in dic:
                total += dic[photo[r][c]]
        answer.append(total)
        
    return answer