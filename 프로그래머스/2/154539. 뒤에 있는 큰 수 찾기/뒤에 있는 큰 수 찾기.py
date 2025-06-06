def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)-1, -1, -1):
        # candidates = [n for n in numbers[i+1:] if n > numbers[i]]
        # answer.append(candidates[0] if candidates else -1)
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
            
        if stack:
            answer[i] = stack[-1]
            
        stack.append(numbers[i])
        
    return answer
