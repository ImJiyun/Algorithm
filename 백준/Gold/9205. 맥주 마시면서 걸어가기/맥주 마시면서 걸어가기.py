import sys
from collections import deque 
input = sys.stdin.readline

def is_near(cur_x, cur_y, dest_x, dest_y, beer):
    return abs(cur_x - dest_x) + abs(cur_y - dest_y) <= beer * 50

def bfs(start_x, start_y, dest_x, dest_y, convenients, beer):
    q = deque([(start_x, start_y)])
    visited = [False] * len(convenients)
    
    while q:
        cur_x, cur_y = q.popleft()
        
        if is_near(cur_x, cur_y, dest_x, dest_y, beer):
            return True

        for i, (con_x, con_y) in enumerate(convenients):
            if is_near(cur_x, cur_y, con_x, con_y, beer) and not visited[i]:
                visited[i] = True
                q.append((con_x, con_y))
    return False            
                
t = int(input())

for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    convenients = [list(map(int, input().split())) for _ in range(n)]
    dest_x, dest_y = map(int, input().split())
    
    beer = 20
    is_found = bfs(start_x, start_y, dest_x, dest_y, convenients, beer)
    
    print('happy' if is_found else 'sad')