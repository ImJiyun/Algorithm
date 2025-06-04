from collections import deque

def solution(x, y, n):
    
    queue = deque([(x, 0)])
    visited = set([x])
    
    while queue:
        num, cnt = queue.popleft()
        
        if num == y:
            return cnt
        
        for nxt in [num + n, num * 2, num * 3]:
            if nxt <= y and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, cnt + 1))
        
    return -1 