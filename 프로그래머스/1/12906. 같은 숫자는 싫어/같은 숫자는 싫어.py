from collections import deque

def solution(arr):
    ans = []
    
    q = deque(arr)
    
    while q:
        num = q.popleft()
        
        if not ans:
            ans.append(num)
        else:
            if ans[-1] == num:
                continue
            else:
                ans.append(num)
    
    return ans