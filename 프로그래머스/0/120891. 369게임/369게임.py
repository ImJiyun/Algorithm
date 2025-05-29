def solution(order):
    answer = 0
    
    nums = ['3', '6', '9']
    for ch in str(order):
        if ch in nums:
            answer += 1
        
    return answer