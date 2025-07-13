def solution(ingredient):
    answer = 0
    stack = []
    
    for item in ingredient:   
        stack.append(item)
        if stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            answer += 1    
    return answer