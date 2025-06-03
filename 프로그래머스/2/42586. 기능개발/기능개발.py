from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    
    q = deque(days)
    
    while q:
        count = 1
        curr = q.popleft()
        while q and curr >= q[0]:
            q.popleft()
            count += 1
        answer.append(count)
        
    return answer