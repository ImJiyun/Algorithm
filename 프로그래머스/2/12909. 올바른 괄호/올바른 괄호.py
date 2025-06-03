from collections import deque

def solution(s):
    d = deque()
    
    for char in s:
        if char == '(':
            d.append(char)
        else:
            if not d:
                return False
            d.pop()
            
    return not d