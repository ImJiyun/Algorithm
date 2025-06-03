from collections import deque
def solution(priorities, location):
    alphabets = [chr(n) for n in range(65, 65 + len(priorities))]
    queue = deque(list(zip(alphabets, priorities)))
    cnt = 0
    target = alphabets[location]
    
    while queue:
        a, p = queue.popleft()
        
        if any(p < other_p for _, other_p in queue):
            queue.append((a,p))
        else:
            cnt += 1
            if a == target:
                return cnt
            